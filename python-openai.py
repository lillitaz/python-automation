import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "davinci-002",
    "prompt": "Write python script for hello world",
    "max_tokens": 150,
    "temperature": 0.7

}
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed {response.status_code}: {response.json()}")
