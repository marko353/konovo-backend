import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")

def get_jwt_token():
    response = requests.post(f"{BASE_URL}/login", json={"username": USERNAME, "password": PASSWORD})
    if response.status_code == 200:
        return response.json().get("token")
    else:
        return None

def get_products_from_api(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/products", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []
