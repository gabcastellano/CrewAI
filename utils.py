import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "mixtral-8x7b-32768")

groq_client = Groq(api_key=GROQ_API_KEY)

def llm_call(prompt: str, max_tokens: int = 800):
    """
    Função de chamada ao modelo Mixtral via Groq.
    Retorna a resposta como string.
    """
    response = groq_client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful AI agent."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=0.2,
    )

    return response.choices[0].message["content"]
