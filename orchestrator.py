import asyncio
import os
from typing import List, AsyncGenerator
from langchain_core.messages import BaseMessage
from providers import create_groq, create_gemini
from routing import select_provider

# Concurrency control
MAX_CONCURRENT_REQUESTS = int(os.getenv("MAX_CONCURRENT_REQUESTS"))
LLM_RETRIES = int(os.getenv("LLM_RETRIES"))
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

PROVIDERS = {"groq": create_groq, "gemini": create_gemini}

# Streaming with retry and fallback
async def orchestrated_stream(messages: List[BaseMessage], retries: int = LLM_RETRIES) -> AsyncGenerator:
    primary = select_provider()
    fallback = "gemini" if primary == "groq" else "groq"

    for provider in [primary, fallback]:
        print(f"🚀 Trying provider: {provider}")
        for attempt in range(retries):
            try:
                llm = PROVIDERS[provider]()
                async for chunk in llm.astream(messages):
                    yield chunk
                return
            except Exception as e:
                print(f"⚠️ {provider} failed (attempt {attempt+1}): {e}")
                await asyncio.sleep(1)

    raise RuntimeError("All providers failed after retries")

# Queue wrapper
async def limited_stream(messages: List[BaseMessage]):
    async with semaphore:
        async for chunk in orchestrated_stream(messages):
            yield chunk
