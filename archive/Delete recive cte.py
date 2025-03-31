import requests

# Replace with your actual API details
base_url = (
    "http://fsma-loadbalancer-1104915305.us-east-2.elb.amazonaws.com/api/v1/cte/receive"
)
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJmb29kX2J1c19pZCI6MiwibG9jYXRpb25faWQiOjIsImZzbWFfdXNlcl9pZCI6Miwic3ViIjoidXNlcjBAZm9vZHRyYWNlYWkuY29tIiwiaWF0IjoxNzQyNTczNTU0LCJleHAiOjE3NDI1ODA3NTR9.jsFOLgwh2hoNVMLe38BKPrFEESMvgGzYY-LSYodfSAA"  # Replace with your actual token
}

# Fetch all records
try:
    response = requests.get(f"{base_url}/findAll", headers=headers)
    if response.status_code == 200:
        records = response.json()
        print(f"Fetched {len(records)} records.")

        # Delete records
        for record in records:
            record_id = record.get("id")
            if record_id is not None:
                delete_url = f"{base_url}/{record_id}"
                try:
                    delete_response = requests.delete(delete_url, headers=headers)
                    if delete_response.status_code in [
                        200,
                        204,
                    ]:  # Treat 204 as success
                        print(f"Successfully deleted record with ID: {record_id}")
                    else:
                        print(
                            f"Failed to delete record with ID: {record_id}. "
                            f"Status Code: {delete_response.status_code}, Response: {delete_response.text}"
                        )
                except Exception as e:
                    print(
                        f"An error occurred while deleting record with ID: {record_id}. Error: {e}"
                    )
            else:
                print("Record does not have an ID, skipping deletion.")
    else:
        print(
            f"Failed to fetch records. Status Code: {response.status_code}, Response: {response.text}"
        )
except Exception as e:
    print(f"An error occurred while fetching records. Error: {e}")
