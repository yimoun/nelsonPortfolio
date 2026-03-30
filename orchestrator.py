import asyncio
import os
from typing import List, AsyncGenerator
from langchain_core.messages import BaseMessage
from providers import create_groq, create_local, ENVIRONMENT
from routing import select_provider, provider_usage

# Concurrency control
MAX_CONCURRENT_REQUESTS = int(os.getenv("MAX_CONCURRENT_REQUESTS"))
LLM_RETRIES = int(os.getenv("LLM_RETRIES"))
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

# Streaming with retry, fallback, queue
async def orchestrated_stream(messages: List[BaseMessage], retries: int = LLM_RETRIES) -> AsyncGenerator:
    tried = set()
    for _ in range(len(provider_usage)):
        provider = select_provider(messages)
        if provider in tried:
            continue
        tried.add(provider)
        print(f"🚀 Trying provider: {provider}")

        for attempt in range(retries):
            try:
                if provider == "groq":
                    llm = create_groq()
                else:
                    llm = create_local()
                provider_usage[provider] += 1
                async for chunk in llm.astream(messages):
                    yield chunk
                return
            except Exception as e:
                print(f"⚠️ {provider} failed (attempt {attempt+1}): {e}")
                await asyncio.sleep(1)

    # Final fallback → only in local (switch to Groq when LM Studio fails)
    if ENVIRONMENT == "local":
        print("⚠️ Local provider failed → fallback Groq")
        llm = create_groq()
        async for chunk in llm.astream(messages):
            yield chunk
    else:
        raise RuntimeError("All providers failed — no fallback available in production")

# Queue wrapper
async def limited_stream(messages: List[BaseMessage]):
    async with semaphore:
        async for chunk in orchestrated_stream(messages):
            yield chunk
