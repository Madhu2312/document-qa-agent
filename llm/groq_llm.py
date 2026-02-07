import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")

    return Groq(api_key=api_key)


def generate_answer(context: str, question: str) -> str:
    client = get_groq_client()

    prompt = f"""
You are a document question answering assistant.

You are given extracted content from a PDF document.
Assume the document is real and authoritative.

Context:
{context}

Question:
{question}

Instructions:
- Answer strictly based on the context
- Do NOT mention missing context or uncertainty
- If the answer is not explicitly found, say: "Not found in the document"
"""


    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
