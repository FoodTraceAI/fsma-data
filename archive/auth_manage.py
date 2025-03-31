# auth_manager.py
import requests
import json

def get_auth_token():
    # Check if token is already saved
    try:
        with open("auth_token.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        pass
    
    # Fetch new token
    url = "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/auth/login"
    payload = {"email": "user0@foodtraceai.com", "password": "123"}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code, "RES CODE")
    if response.status_code == 200:
        token = response.json().get("token")
        with open("auth_token.txt", "w") as file:
            file.write(token)
        return token
    else:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")
# testing a new change for push