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

def fetch_github_issues(owner, repo):
    data = fetch_github(owner, repo, "issues")
    return load_issues(data)

def load_issues(issues):
    docs = []
    for entry in issues:
        metadata = {
            "author": entry["user"] ["login"],
            "comments": entry["comments"],
            "body": entry["body"],
            "labels": entry["labels"],
            "created_at": entry["created_at"]
        }
        # Concatinating title and body
        data = entry["title"]
        if entry["body"]:
            data += entry["body"]
        doc = Document(page_content=data, metadata=metadata)
        docs.append(doc)
    
    return docs


# Example usage
owner = "LorenzoBalderrama"
repo = "Go-Microservices-for-a-OMS"
endpoint = "issues"

fetch_github(owner, repo, endpoint)
