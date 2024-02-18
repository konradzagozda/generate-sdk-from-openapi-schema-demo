from fastapi import FastAPI

from .router import router as posts_router

app = FastAPI()

app.include_router(posts_router, tags=["posts"])
