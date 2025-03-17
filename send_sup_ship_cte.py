# import requests
# from datetime import datetime, timezone

# # Define the API endpoint
# url = "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/supplier/shipCte"

# # Define the headers
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJmb29kX2J1c19pZCI6MiwibG9jYXRpb25faWQiOjIsImZzbWFfdXNlcl9pZCI6Miwic3ViIjoidXNlcjBAZm9vZHRyYWNlYWkuY29tIiwiaWF0IjoxNzM3NjYzMjEzLCJleHAiOjE3Mzc2NzA0MTN9.dW2C0oe7SR9sD1veMpfpF-Y3j_v3SZfRutG3XU77bBE"  # Replace with your actual access token if required
# }

# # Generate the current date and time
# current_time = datetime.now(timezone.utc)
# current_date = current_time.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
# iso_timestamp = current_time.isoformat()  # ISO format with timezone information

# # Define the payload with dynamically generated date and time
# payload = {
#     "sscc": "ABC12345",
#     "logSerialNo": "LOG001",
#     "supCteStatus": "Pending",
#     "ftlItem": "Bivalves",
#     "variety": "Standard",
#     "tlcId": 1,
#     "quantity": 100,
#     "unitOfMeasure": "Bin",
#     "prodDesc": "Fresh Bivalves",
#     "shipToLocationId": 2,
#     "shipFromLocationId": 3,
#     "shipDate": current_date,  # Use current date
#     "tlcSourceId": 2,
#     "tlcSourceReference": "SRC001",
#     "referenceDocumentType": "ASN",
#     "referenceDocumentNum": "DOC001",
#     "dateCreated": iso_timestamp,  # Use current timestamp with timezone
#     "dateModified": iso_timestamp,  # Use current timestamp with timezone
#     "isDeleted": False,
#     "dateDeleted": None
# }

# # Make the POST request
# response = requests.post(url, json=payload, headers=headers)

# # Check the response
# if response.status_code in [200, 201]:  
#     print("Supplier shipping CTE created successfully!")
#     print("Response:", response.json())
# else:
#     print("Failed to create record.")
#     print("Status Code:", response.status_code)
#     print("Response:", response.json())
import requests
from datetime import datetime, timezone
import os

# Define the API endpoint
url = "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/supplier/shipcte"

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJmb29kX2J1c19pZCI6MiwibG9jYXRpb25faWQiOjIsImZzbWFfdXNlcl9pZCI6Miwic3ViIjoidXNlcjBAZm9vZHRyYWNlYWkuY29tIiwiaWF0IjoxNzM4NzAzMjEwLCJleHAiOjE3Mzg3MTA0MTB9.8s20UGX_szSZIc51aQG-qAlhdnpliuJlXFKh1N4kwbw"  # Replace with your actual access token if required
}

# File to store the last SSCC value
sscc_file = "last_sscc.txt"

# Function to get the next sequential SSCC
def get_next_sscc(prefix="ABC"):
    # Check if the file exists
    if os.path.exists(sscc_file):
        with open(sscc_file, "r") as file:
            last_sscc = file.read().strip()
        # Extract the numeric part and increment it
        last_number = int(last_sscc[len(prefix):])
        next_number = last_number + 1
    else:
        # If the file doesn't exist, start from 1
        next_number = 1

    # Construct the new SSCC
    next_sscc = f"{prefix}{next_number}"
    
    # Save the new SSCC back to the file
    with open(sscc_file, "w") as file:
        file.write(next_sscc)
    
    return next_sscc

# Generate the current date and time
current_time = datetime.now(timezone.utc)
current_date = current_time.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
iso_timestamp = current_time.isoformat()  # ISO format with timezone information

# Get the next sequential SSCC
unique_sscc = get_next_sscc()

# Define the payload with dynamically generated date and time
payload = {
    "sscc": unique_sscc,  # Use dynamically generated unique SSCC
    "logSerialNo": "LOG001",
    "supCteStatus": "Pending",
    "ftlItem": "Bivalves",
    "variety": "Standard",
    "tlcId": 1,
    "quantity": 100,
    "unitOfMeasure": "Bin",
    "prodDesc": "Fresh Bivalves",
    "shipToLocationId": 2,
    "shipFromLocationId": 1,
    "shipDate": current_date,  # Use current date
    "tlcSourceId": 2,
    "tlcSourceReference": "SRC001",
    "referenceDocumentType": "ASN",
    "referenceDocumentNum": "DOC001",
    "dateCreated": iso_timestamp,  # Use current timestamp with timezone
    "dateModified": iso_timestamp,  # Use current timestamp with timezone
    "isDeleted": False,
    "dateDeleted": None
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code in [200, 201]:  
    print("Supplier shipping CTE created successfully!")
    print("SSCC:", unique_sscc)
    print("Response:", response.json())
else:
    print("Failed to create record.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
