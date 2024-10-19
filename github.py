import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load GitHub token from environment
github_token = os.getenv("GITHUB_TOKEN")

# Function to dynamically fetch data from GitHub (issues, pulls, etc.)
def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed with status code:", response.status_code)
        return []
    
    print(data)
    return data



# Example usage

owner = ""
repo = ""
endpoint = ""

fetch_github(owner, repo, endpoint)
