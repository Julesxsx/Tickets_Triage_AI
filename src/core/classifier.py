import ollama
from src.models.ticket_schema import CategorizedTicket

SYSTEM_PROMPT = """
You are a Lead Support Strategist. Categorize tickets based on these strict rules:
- Technical issue: Bugs, errors, login/account access, or hardware glitches.
- Billing inquiry: Questions about invoices, payments, or unexpected charges.
- Product inquiry: General questions about how a product works.
- Refund request: Explicitly asking for money back.
- Cancellation request: Wanting to end a subscription or service.

Ignore boilerplate text like 'Please assist' or 'zip code'. Focus on the core user problem.
"""

def triage_ticket(ticket_text: str, model_name: str = "phi4-mini"):
    """
    Categorizes a single ticket using local SLM with Few-Shot prompting.
    """
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        
        {"role": "user", "content": "I want a refund for the broken TV I bought last week."},
        {"role": "assistant", "content": '{"intent": "Refund request", "priority": "High", "summary": "Customer requesting refund for damaged TV."}'},
        {"role": "user", "content": "I can't log in to my account, it keeps saying invalid password."},
        {"role": "assistant", "content": '{"intent": "Technical issue", "priority": "Urgent", "summary": "User locked out of account due to password error."}'},
        
        {"role": "user", "content": f"Categorize this: {ticket_text}"}
    ]

    try:
        response = ollama.chat(
            model=model_name,
            messages=messages,
            format=CategorizedTicket.model_json_schema(),
            options={"temperature": 0}
        )
        
        return CategorizedTicket.model_validate_json(response.message.content)
    
    except Exception as e:
        print(f"Error during triage: {e}")
        return None