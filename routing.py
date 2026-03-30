# Smart routing
from providers import GROQ_API_KEY, GEMINI_API_KEY

def select_provider() -> str:
    # Groq is the primary provider (faster, free)
    if GROQ_API_KEY:
        return "groq"

    # Gemini as secondary if Groq key is missing
    if GEMINI_API_KEY:
        return "gemini"

    raise ValueError("No API key configured — set GROQ_API_KEY or GEMINI_API_KEY")
