import os
import requests

def list_voices():
    headers = {
        'Authorization': f'Bearer {os.getenv("API_KEY")}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "voice-enrollment",
        "input": {
            "action": "list_voices",
            "page_size": 100,
            "page_index": 0
        }
    }
    response = requests.post(os.getenv("VOICE_URL"), headers=headers, json=data)
    return response.json()
