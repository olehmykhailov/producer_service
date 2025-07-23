import os
import time
import requests

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "5000")
API_PATH = os.getenv("API_PATH", "/api/message")

def send_message():
    url = f'http://{API_HOST}:{API_PORT}{API_PATH}'
    message = 'Hello, World!'
    try:
        response = requests.get(url, params={'message': message})
        print(f"Response: {response.json()}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")

while True:
    send_message()
    time.sleep(5)
