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
@app.get("/weather/data")
def get_data():
    api_url = "https://api.openweathermap.org/data/2.5/weather?lat=40.7128&lon=-74.0060&appid=552e4d84176112065cd3b3b8e9c79017"
    response = requests.get(api_url, timeout=5)
    data = response.json()
    return data