# Création des LLM (Groq, Ollama)
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def create_groq():
    if GROQ_API_KEY:
        return ChatGroq(model="llama-3.3-70b-versatile", streaming=True)
    raise ValueError("GROQ_API_KEY not set")

def create_ollama():
    return ChatOllama(model="qwen2.5", streaming=True)