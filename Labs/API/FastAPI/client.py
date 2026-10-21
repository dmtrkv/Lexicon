import requests
from api_client import get_json
from pprint import pprint

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
    json=new_movie,
    timeout=5
)
print(response.status_code)
pprint(response.json())
