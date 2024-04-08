from fastapi import FastAPI

from src.api.health import controller as health
from src.api.classificator import controller as classificator

app = FastAPI(docs_url="/swagger", redoc_url=None)

app.include_router(health.router)
app.include_router(classificator.router)