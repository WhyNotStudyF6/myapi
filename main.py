import requests
import random
from fastapi import FastAPI

app = FastAPI()

IMGBB_API_KEY = "727af41d4805f56a09ea89ec070e9bd6"
POSTS_JSON = "https://whynotstudyf6.github.io/wfvh/index.json"

@app.get("/api/wfvh")
def get_posts():
    return requests.get(POSTS_JSON).json()

@app.get("/api/wfvh/random")
def get_random_post():
    data = requests.get(POSTS_JSON).json()
    return random.choice(data)

@app.get("/api/images")
def get_images():
    res = requests.get(f"https://api.imgbb.com/1/account/images?key={IMGBB_API_KEY}").json()
    return [img["data"]["url"] for img in res["data"]]

@app.get("/api/images/random")
def get_random_image():
    res = requests.get(f"https://api.imgbb.com/1/account/images?key={IMGBB_API_KEY}").json()
    images = [img["data"]["url"] for img in res["data"]]
    return {"url": random.choice(images)}