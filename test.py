import requests
import os
from dotenv import load_dotenv

load_dotenv()

textInput = input()
payload = {"search_query": textInput}

response = requests.post('http://127.0.0.1:5000', json=payload)
# Check if the request was successful
if response.status_code == 200: # Assuming the response is in JSON format
    print("success!")
else:
    print(f"Request failed with status code: {response.status_code}")