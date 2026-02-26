🎫 Enterprise AI Ticket Triage (Local SLM)

A production-ready customer support classification engine that uses a local Small Language Model (SLM) to automate intent detection, priority assignment, and sentiment analysis.


💡 The Core Problem

Many public support datasets (like those on Kaggle) rely on repetitive templates (e.g., "I am having an issue with {product}") that don't reflect the messy, emotional, and typo-ridden reality of human communication.

This project solves this by:

Local Inference: Running Microsoft Phi-4 Mini via Ollama for 100% data privacy and zero API costs.

Synthetic "Hard Mode" Data: Moving beyond static datasets to a custom-built generation engine that simulates real-world noise: slang, typos, and high-intensity frustration.

Strict Data Contracts: Using Pydantic to enforce structured JSON outputs, ensuring the AI never "hallucinates" a category that doesn't exist in your database.


🛠️ Tech Stack

LLM: Phi-4 Mini (3.8B) via Ollama

Language: Python 3.10+

Validation: Pydantic v2

Data Science: Pandas, Scikit-Learn (for model benchmarking)

Visualization: Seaborn, Matplotlib


📈 Performance & Robustness

I pivoted from the standard Kaggle Customer Support dataset after finding it lacked the linguistic variety needed for modern SLM benchmarking.

"Hard Mode" Validation Results
By injecting "noise" (typos, slang, and emotional filler), I tested the limits of the model's reasoning.

Accuracy: ~88-94% on noisy data.

Key Insight: Implementing Few-Shot Prompting in the core classifier allowed the model to correctly identify "Refund" vs. "Billing" even when the user used highly informal language (e.g., "yo, money gone from my bank").
