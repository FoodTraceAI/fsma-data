import requests
import json

# API endpoint
url = "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/auth/login"

# Request body (update the email and password with correct credentials)
payload = {
    "email": "user0@foodtraceai.com",
    "password": "123"
}

# Headers
headers = {
    "Content-Type": "application/json"
}

try:
    # Send POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Login Successful!")
        print("Response:", response.json())
    else:
        print(f"Login Failed! Status Code: {response.status_code}")
        print("Error Response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")
