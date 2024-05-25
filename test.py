import requests
import os
from dotenv import load_dotenv

load_dotenv()

textInput = input()
payload = {"search_query": textInput}

response = requests.get('http://127.0.0.1:5000', json=payload, stream=True)
with open("returnedVideo.mp3", 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192): 
        # If you have chunk encoded response uncomment if
        # and set chunk_size parameter to None.
        #if chunk: 
        f.write(chunk)

# Check if the request was successful
if response.status_code == 200: # Assuming the response is in JSON format
    print("success!")
else:
    print(f"Request failed with status code: {response.status_code}")