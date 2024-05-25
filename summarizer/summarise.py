import requests 
import os
from dotenv import load_dotenv

load_dotenv()

def summarise(text): 
    payload = {'text': text}
    headers = {'x-api-key': os.getenv("jigsaw_key")}

    response = requests.post('https://api.jigsawstack.com/v1/ai/summary', json=payload, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()["summary"]  # Assuming the response is in JSON format
        print(data)
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        return 0

def translate(text, currLang, targetLang): 
    payload = {'text': text, "current_language": currLang, "target_language": targetLang}
    headers = {'x-api-key': os.getenv("jigsaw_key")}

    response = requests.post('https://api.jigsawstack.com/v1/ai/translate', json=payload, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()["translated_text"]  # Assuming the response is in JSON format
        print(data)
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        return 0


#file = open("newsarticle.txt", "r").read()
#summarisedText = summarise(file)
#translate(summarisedText, "en", "ch")