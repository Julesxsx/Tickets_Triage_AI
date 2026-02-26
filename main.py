import pandas as pd
from src.core.classifier import triage_ticket
from sklearn.metrics import classification_report
import os

def run_pipeline(input_file, output_file, limit=20):
    print(f"🚀 Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    
    ai_intents = []
    ai_priorities = []
    
    print(f"🤖 Processing {limit} tickets using Local SLM...")
    
    for i, row in df.iterrows():
        result = triage_ticket(row['Ticket Description'])
        
        if result:
            ai_intents.append(result.intent)
            ai_priorities.append(result.priority)
        else:
            ai_intents.append(None)
            ai_priorities.append(None)
            
        if (i + 1) % 5 == 0:
            print(f"✅ Completed {i + 1}/{limit}...")

    df['AI_Intent'] = ai_intents
    df['AI_Priority'] = ai_priorities
    
    df.to_csv(output_file, index=False)
    print(f"💾 Results saved to {output_file}")
    
    if 'Ticket Type' in df.columns:
        print("\n--- PERFORMANCE REPORT ---")
        report_df = df.dropna(subset=['AI_Intent'])
        print(classification_report(report_df['Ticket Type'], report_df['AI_Intent']))

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
        
    INPUT = 'data/synthetic_tickets_hard.csv'
    OUTPUT = 'data/processed_results.csv'
    
    run_pipeline(INPUT, OUTPUT, limit=2000)