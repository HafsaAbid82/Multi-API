from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or ["http://localhost:5173"] for your Vite app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/quotes/data")
def get_data():
    api_url = "https://zenquotes.io/api/random"
    response = requests.get(api_url, timeout=5)
    data = response.json()
    return data