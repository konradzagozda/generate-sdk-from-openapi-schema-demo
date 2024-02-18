from random import randrange

from fastapi import APIRouter, HTTPException, status

from .data import posts
from .helpers import find_index_post, find_post
from .models import Post

router = APIRouter(prefix="/posts")


@router.get("/", response_model=list[Post])
def get_all_posts():
    return posts


@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    posts.append(post_dict)
    return post_dict


@router.get("/latest", response_model=Post)
def get_latest_post():
    post = posts[-1]
    return post


@router.get("/{id}", response_model=Post)
def get_post_by_id(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found"
        )
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist",
        )
    posts.pop(indx)
    return True


@router.put("/{id}", response_model=Post)
def update_post(id: int, post: Post):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist",
        )
    post_dict = post.dict()
    post_dict["id"] = id
    posts[indx] = post_dict
    return post_dict
