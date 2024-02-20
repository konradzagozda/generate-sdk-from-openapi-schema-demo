from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


class PostGet(Post):
    id: int
