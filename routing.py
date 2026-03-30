
# Smart routing / load balancingfrom typing import List
from langchain_core.messages import BaseMessage

# Simple load tracking
provider_usage = {"groq": 0, "ollama": 0}

def get_least_used_provider():
    return min(provider_usage, key=provider_usage.get)

# Smart routing (conversation length)
def select_provider(messages: List[BaseMessage]) -> str:
    last_msg = messages[-1].content.lower()
    
    if len(last_msg) < 50:
        return "ollama"  # short/simple message
    return get_least_used_provider()