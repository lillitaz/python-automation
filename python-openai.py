import requests
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

prompt = input("What script do you need: ")
file_name = input("Enter the file name to save the script (don't forget the .py at the end): ")

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"You are a python developer with 20 years of experience. Write a python script to {prompt}. Provide only code, no text.",
    "max_tokens": 1000,
    "temperature": 0.7

}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed {response.status_code}: {response.json()}")

try:
    subprocess.run(['python3', file_name], check=True)
except subprocess.CalledProcessError as error:
    print(f"Script execution failed with error: {error}")
