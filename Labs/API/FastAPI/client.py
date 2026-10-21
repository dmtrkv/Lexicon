import requests
from api_client import get_json
from pprint import pprint

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API key is missing.")

base_url = "http://127.0.0.1:8000"

movies = get_json(f"{base_url}/movies")
pprint(movies)

get_json(
    f"{base_url}/movies/99"  # 404
)

new_movie = {
    "id": 5,
    "title": "Title",
    "director": "Director",
    "year": 2026
}
response = requests.post(
    f"{base_url}/movies",
    headers={"X-API-Key": API_KEY},
    json=new_movie,
    timeout=5
)
print(response.status_code)
pprint(response.json())
