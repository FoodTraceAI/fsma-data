import psycopg2
from psycopg2.extras import RealDictCursor

# Database connection parameters
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "gotdac-gevtaw-vuzQu9",
    "host": "fsma-pg.ch2qgmggwb17.us-east-2.rds.amazonaws.com",
    "port": "5432"
}

def verify_ship_to_location(ship_to_location_id):
    """
    Verifies if the given `ship_to_location_id` exists in the `location` table.
    """
    try:
        # Connect to the database
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                # Query to check if the ship_to_location_id exists
                query = "SELECT id FROM public.location WHERE id = %s"
                cursor.execute(query, (ship_to_location_id,))
                result = cursor.fetchone()

                if result:
                    print(f"ship_to_location_id {ship_to_location_id} exists in the database.")
                    return True
                else:
                    print(f"ship_to_location_id {ship_to_location_id} does NOT exist in the database.")
                    return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def handle_api_request(payload):
    """
    Handles the API request payload, verifies ship_to_location_id, and returns an appropriate response.
    """
    ship_to_location_id = payload.get("shipToLocationId")

    # Verify if the ship_to_location_id exists
    if not verify_ship_to_location(ship_to_location_id):
        return {
            "status": "error",
            "message": f"Invalid shipToLocationId: {ship_to_location_id}. Please provide a valid ID."
        }

    # Validate other fields (if necessary)
    # Example: Check if cte_type is valid
    allowed_cte_types = [
        "Cool", "Harvest", "InitPackExempt", "InitPackProduce",
        "InitPackSprouts", "FirstLandReceive", "Ship", "Receive",
        "ReceiveExempt", "Transform"
    ]
    cte_type = payload.get("cteType")
    if cte_type not in allowed_cte_types:
        return {
            "status": "error",
            "message": f"Invalid cteType: {cte_type}. Allowed types are {allowed_cte_types}."
        }

    # If all checks pass, return success
    return {
        "status": "success",
        "message": "Payload is valid and ready for processing."
    }

# Example API payload
example_payload = {
    "shipToLocationId": 3,  # Replace with the actual ID to test
    "cteType": "Ship"
}

# Process the API request
response = handle_api_request(example_payload)
print(response)
