import requests
import random
from fastapi import FastAPI

app = FastAPI()

BLOG_JSON = "https://whynotstudyf6.github.io/index.json"

@app.get("/api/posts")
def get_posts():
    data = requests.get(BLOG_JSON).json()
    return data

@app.get("/api/posts/random")
def get_random_post():
    data = requests.get(BLOG_JSON).json()
    return random.choice(data)

@app.get("/api/posts/{title}")
def get_post(title: str):
    data = requests.get(BLOG_JSON).json()
    for post in data:
        if title in post["permalink"]:
            return post
    return {"error": "找不到文章"}
