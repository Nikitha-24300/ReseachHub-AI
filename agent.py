from groq import Groq
import os
from dotenv import load_dotenv
from .rag_pipeline import build_context

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(question: str):
    context = build_context(question)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"You are a research assistant. Context: {context}"},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content