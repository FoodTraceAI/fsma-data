import requests
import json
from datetime import datetime

# API Endpoint for creating Shipping CTE
api_url = "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/cte/ship"

# New Access Token
access_token = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJmb29kX2J1c19pZCI6MiwibG9jYXRpb25faWQiOjIsImZzbWFfdXNlcl9pZCI6Miwic3ViIjoidXNlcjBAZm9vZHRyYWNlYWkuY29tIiwiaWF0IjoxNzM3MjM4MjM5LCJleHAiOjE3MzcyNDU0Mzl9.yzhMScHJf6dsrUpGvTtI8NLiFYDjsy6tjeY0y8pLPYE"

# Headers
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

# Get current date and time in ISO format
current_datetime = datetime.utcnow().isoformat() + "Z"
current_date = datetime.utcnow().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
current_time = datetime.utcnow().isoformat() + "Z"  # Current date and time in ISO format

# Payload with corrected field names
payload = {
    "cteType": "Cool",
    "ftlItem": "Cucumbers",
    "tlcId": 1,
    "quantity": 10,
    "unitOfMeasure": "Bin",  # Corrected field
    "prodDesc": "Fresh Cucumbers",
    "variety": "Organic",
    "shipToLocationId": 3,
    "locationId": 2,
    "shipDate": current_date,  # Dynamic ship date
    "shipTime": current_time,  # Dynamic ship time
    "tlcSourceId": 1,
    "tlcSourceReference": "REF123",
    "referenceDocumentType": "ASN",
    "referenceDocumentNum": "DOC12345",
    "dateCreated": current_datetime,  # Use current date and time
    "dateModified": current_datetime,  # Use current date and time
    "isDeleted": False,
    "dateDeleted": None
}

# Make the API Request
try:
    print("Sending request to create Shipping CTE...")
    response = requests.post(api_url, headers=headers, json=payload)

    # Check response status
    if response.status_code in [200, 201]:
        print("Shipping CTE Created Successfully!")
        print("Response:", response.json())
    else:
        print("Failed to Create Shipping CTE. Status Code:", response.status_code)
        print("Error Response:", response.text)

except Exception as e:
    print("An error occurred:", e)

