import pandas as pd
import ollama
from src.models.ticket_schema import CategorizedTicket

def process_tickets(input_path, output_path, sample_size=10):

    df = pd.read_csv(input_path)
    subset = df.head(sample_size).copy()
    
    results = []
    
    print(f"Starting batch processing for {sample_size} tickets...")
    
    for index, row in subset.iterrows():
        text = row['Ticket Description']
        
        try:
            response = ollama.chat(
                model='phi4-mini',
                messages=[{'role': 'user', 'content': f"Categorize: {text}"}],
                format=CategorizedTicket.model_json_schema()
            )
            
            analysis = CategorizedTicket.model_validate_json(response.message.content)
            results.append(analysis.model_dump())
            print(f"Processed Ticket {index+1}/{sample_size}")
            
        except Exception as e:
            print(f"Error on ticket {index}: {e}")
            results.append(None)
    res_df = pd.DataFrame([r for r in results if r is not None])
    final_df = pd.concat([subset.reset_index(drop=True), res_df], axis=1)
    
    final_df.to_csv(output_path, index=False)
    print(f"Success! Saved to {output_path}")

if __name__ == "__main__":
    process_tickets('data/raw_tickets.csv', 'data/processed_tickets.csv')