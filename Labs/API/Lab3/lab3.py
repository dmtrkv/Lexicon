# from Labs/ python -m API.Lab3.lab3

from ..api import get_json

# GET https://api.github.com/users/<username>/repos
#  params: sort=pushed, per_page=5
#  header: Authorization: Bearer <token>

# 1 Create a token
# Log in to github.com. Click your profile picture, choose Settings, scroll down in the left
# menu and click Developer settings. Choose Personal access tokens, then Tokens
# (classic), then Generate new token (classic). Name it api-course and pick a short
# expiry, for example 7 days. Do not tick any scopes, because we only read public
# information. Click Generate token and copy it right away. GitHub shows it only once.
# (GitHub sometimes renames menus. If something does not match, look for the names in
# bold.)
pass

# 2 Store it safely
# In a new folder, create .gitignore first and put .env in it. Then create .env and write
# GITHUB_TOKEN=your_token in it, with no quotes. Do not paste the token in chat, do not
# take a screenshot of it, and do not share your screen while it is visible.
pass

# 3 Call the API with the token
# Load the token with load_dotenv() and os.getenv("GITHUB_TOKEN"). Send it in the
# header Authorization: Bearer <token>. Ask for a GitHub username with input(),
# call the endpoint above, and print the name of each repository. Use get_json from
# api_client.py.
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN is missing.")

username = input("Username: ")
repos = get_json(
    f"https://api.github.com/users/{username}/repos",
    params={"sort": "pushed", "per_page": 5},
    headers={"Authorization": f"Bearer {token}"}
)

if repos:
    for repo in repos:
        print(repo["name"])
else:
    print("No repos.")

# 4 Prove that the token is used
# Look at the response headers. Print X-RateLimit-Limit with and without the token.
# With the token it should say 5000, without it 60. Hint: you need the whole response for
# this, so call requests.get directly.
import requests

response = requests.get(
    f"https://api.github.com/users/{username}/repos",
    params={"sort": "pushed", "per_page": 5},
    headers={"Authorization": f"Bearer {token}"},
)
print("With token:", response.headers.get("X-RateLimit-Limit"))

response = requests.get(
    f"https://api.github.com/users/{username}/repos", 
    params={"sort": "pushed", "per_page": 5})
print("Without token:", response.headers.get("X-RateLimit-Limit"))

# 5 Break the token on purpose
# Change one character in your token and run the program again. Which status code do
# you get, and what does the message say? Expected: status 401 and a message about
# bad credentials. Is that 401 or 403, and what is the difference? Then fix the token again.
get_json(
    f"https://api.github.com/users/{username}/repos",
    params={"sort": "pushed", "per_page": 5},
    headers={"Authorization": f"Bearer ???"}
) # 401 - Unauthorized (I don't know, who you are)
# 403 - Forbidden (I do know, who you are, but the action is forbidden)

# 6 Check that the secret is safe
# Run git init and then git status in your folder. The file .env must not appear in the
# list. If it does, your .gitignore is wrong. Fix it before you do anything else.
pass

# 7 Delete the token
# When you are done, go back to the token page on GitHub and delete the token.
pass
