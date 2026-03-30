# Création des LLM (Groq, LM Studio)
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
print(f"🔑 GROQ_API_KEY loaded: {'Yes' if GROQ_API_KEY else 'No'}")
print(f"🌍 Environment: {ENVIRONMENT}")

def create_groq():
    if GROQ_API_KEY:
        return ChatGroq(model="llama-3.3-70b-versatile", streaming=True)
    raise ValueError("GROQ_API_KEY not set")

def create_local():
    return ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        streaming=True,
    )
