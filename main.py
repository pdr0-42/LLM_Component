from fastapi import FastAPI

from src.router.completion import LLMRouter

app = FastAPI()

app.include_router(LLMRouter)
