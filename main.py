import requests
import random
from fastapi import FastAPI

app = FastAPI()

POSTS_JSON = "https://whynotstudyf6.github.io/wfvh/index.json"
IMAGES_JSON = "https://whynotstudyf6.github.io/images.json"

@app.get("/api/posts")
def get_posts():
    return requests.get(POSTS_JSON).json()

@app.get("/api/posts/random")
def get_random_post():
    data = requests.get(POSTS_JSON).json()
    return random.choice(data)

@app.get("/api/posts/{category}")
def get_category(category: str):
    url = f"https://whynotstudyf6.github.io/wfvh/{category}/index.json"
    return requests.get(url).json()

@app.get("/api/images")
def get_images():
    return requests.get(IMAGES_JSON).json()

@app.get("/api/images/random")
def get_random_image():
    data = requests.get(IMAGES_JSON).json()
    return {"url": "https://whynotstudyf6.github.io" + random.choice(data)}