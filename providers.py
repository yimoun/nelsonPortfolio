# Création des LLM (Groq + Gemini)
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(f"🔑 GROQ_API_KEY loaded: {'Yes' if GROQ_API_KEY else 'No'}")
print(f"🔑 GEMINI_API_KEY loaded: {'Yes' if GEMINI_API_KEY else 'No'}")

def create_groq():
    if GROQ_API_KEY:
        return ChatGroq(model="llama-3.3-70b-versatile", streaming=True)
    raise ValueError("GROQ_API_KEY not set")

def create_gemini():
    if GEMINI_API_KEY:
        return ChatGoogleGenerativeAI(model="gemini-2.0-flash", streaming=True)
    raise ValueError("GEMINI_API_KEY not set")
