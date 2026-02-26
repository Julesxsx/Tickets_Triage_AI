import pandas as pd
import random

categories = {
    "Technical issue": [
        "screen is black again. i tried to reset it but nothing. total brick.",
        "firmware update failed 404. {product} won't turn on now. fix this.",
        "it keeps crashing when i open the settings... why??",
        "wont connect to wifi. every other device works fine. {product} is junk.",
        "battery draining 20% in 5 mins. its literally hot to the touch."
    ],
    "Billing inquiry": [
        "yo, i saw a $49 charge on my card but i canceled last month??",
        "u guys charged me twice for the same {product}. give it back.",
        "where is my receipt? i need it for my taxes like now.",
        "credit card declined but the money is gone from my bank account.",
        "can i change my paymnt method? the current card is expired."
    ],
    "Refund request": [
        "i want a refund. the {product} is trash and doesnt work.",
        "returning this. i found it cheaper somewhere else. money back plz.",
        "it arrived broken. box was crushed. i want my money back ASAP.",
        "not what i expected. how do i get a refund?",
        "been 2 weeks and still no refund in my account. where is it?"
    ],
    "Cancellation request": [
        "stop the subscription. i dont use this anymore.",
        "cancel my account immediately. do not charge me again.",
        "how do i opt out of the auto-renew? i want out.",
        "close my profile and delete my data. thx.",
        "pls terminate my membership. too expensive now."
    ],
    "Product inquiry": [
        "does this {product} work with iphone 15?",
        "whats the diff between the blue and red models?",
        "is the {product} waterproof or just splash proof?",
        "do u ship to delhi? how long does it take?",
        "can i use this without a subscription?"
    ]
}

products = ["Smart Watch", "Laptop", "Buds", "Console", "E-Reader"]
priorities = ["Low", "Medium", "High", "Critical"]

def add_noise(text):
    fillers = ["Ugh,", "PLEASE HELP!!!", "I'm so frustrated...", "Worst experience ever.", "???", "Sigh."]
    
    if random.random() < 0.3:
        text = f"{random.choice(fillers)} {text}"
        
    typos = {"account": "accnt", "product": "prodt", "refund": "refnd", "service": "servce", "please": "pls"}
    words = text.split()
    for i, word in enumerate(words):
        clean_word = word.lower().strip(".,!?") 
        if clean_word in typos and random.random() < 0.2:
            words[i] = typos[clean_word]
            
    return " ".join(words)

def generate_hard_mode_csv(count=200):
    data = []
    for i in range(count):
        ticket_type = random.choice(list(categories.keys()))
        template = random.choice(categories[ticket_type])
        product = random.choice(products)
        
        description = template.format(product=product)

        description = add_noise(description)
        
        priority = random.choice(priorities)
        
        data.append({
            "Ticket ID": i + 1,
            "Ticket Type": ticket_type,
            "Ticket Description": description,
            "Ticket Priority": priority
        })
        
    df = pd.DataFrame(data)
    df.to_csv('data/synthetic_tickets_hard.csv', index=False)
    print(f"✅ Generated {count} 'Hard Mode' tickets in 'data/synthetic_tickets_hard.csv'")

if __name__ == "__main__":
    generate_hard_mode_csv(200)