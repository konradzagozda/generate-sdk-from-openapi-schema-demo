from fastapi import FastAPI
from fastapi.routing import APIRoute

from .router import router as posts_router


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)

app.include_router(posts_router, tags=["posts"])
