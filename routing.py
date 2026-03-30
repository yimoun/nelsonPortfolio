# Smart routing / load balancing
from typing import List
from langchain_core.messages import BaseMessage
from providers import ENVIRONMENT

# Simple load tracking
provider_usage = {"groq": 0, "local": 0}

def select_provider(messages: List[BaseMessage]) -> str:
    # Production → Groq only (no local server available)
    if ENVIRONMENT == "production":
        return "groq"

    # Local → prefer local (LM Studio), fallback to Groq
    return "local"
