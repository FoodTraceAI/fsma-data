import requests

# Base URL and headers
base_url = (
    "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/supshipcte"
)
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJmb29kX2J1c19pZCI6MiwibG9jYXRpb25faWQiOjIsImZzbWFfdXNlcl9pZCI6Miwic3ViIjoidXNlcjBAZm9vZHRyYWNlYWkuY29tIiwiaWF0IjoxNzQyNTczNTU0LCJleHAiOjE3NDI1ODA3NTR9.jsFOLgwh2hoNVMLe38BKPrFEESMvgGzYY-LSYodfSAA",  # Replace with your token
    "Content-Type": "application/json",
}

# Step 1: Fetch all records
fetch_url = f"{base_url}/findAll"
response = requests.get(fetch_url, headers=headers)

if response.status_code == 200:
    records = response.json()  # Assuming the response returns a JSON array
    print(f"Fetched {len(records)} records.")

    # Step 2: Delete each record
    for record in records:
        record_id = record.get("id")
        if record_id is not None:
            delete_url = f"{base_url}/{record_id}"
            delete_response = requests.delete(delete_url, headers=headers)

            if delete_response.status_code in [200, 204]:
                print(f"Successfully deleted record with ID: {record_id}")
            else:
                print(
                    f"Failed to delete record with ID: {record_id}. "
                    f"Status Code: {delete_response.status_code}, Response: {delete_response.text}"
                )
else:
    print(
        f"Failed to fetch records. Status Code: {response.status_code}, Response: {response.text}"
    )
