import requests

# API URL for login
api_url = "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/auth/login"
# api_url = "http://127.0.0.1:8080/api/v1/auth/login"

# Login credentials
payload = {
    "email": "user0@foodtraceai.com",  # Your username
    "password": "123",  # Your password
    # "refreshToken": "",  # Leave this blank for now
}

# Headers
headers = {"Content-Type": "application/json"}  # Specify JSON data

# Call the Login API
try:
    print("Attempting to log in...")
    response = requests.post(api_url, json=payload, headers=headers)
    # response = requests.post(api_url, auth=(payload["email"], payload["password"]))

    # Check if login was successful
    if response.status_code == 200:
        print("Login Successful!")
        response_data = response.json()
        print("Response Data:", response_data)

        # Extract the access token
        access_token = response_data.get("accessToken")
        if access_token:
            print("Access Token:", access_token)
        else:
            print("No access token found in the response.")
    else:
        print("Login Failed! Status Code:", response.status_code)
        print("Error Response:", response.text)

except Exception as e:
    print("An error occurred:", e)
