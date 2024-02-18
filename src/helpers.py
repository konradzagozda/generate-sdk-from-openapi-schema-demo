from .data import posts


def find_post(id):
    for p in posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(posts):
        if p["id"] == id:
            return i
