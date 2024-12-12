# Put Method

import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_booking():
    """Test case to perform a GET request to /booking."""
    booking_id = 3134
    endpoint = f"{BASE_URL}/booking/{booking_id}"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }

    # Sample data to be sent in the POST request
    payload = {
        "firstname": "Amit",
        "lastname": "Tiwari",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-01",
            "checkout": "2024-12-03"
        },
        "additionalneeds": "Dinner"
    }

    # Perform Put request
    response = requests.put(endpoint, headers=headers, json=payload)

    # Log status code
    print(f"Status Code: {response.status_code}")

    # Log response content (body)
    print(f"Response Body: {response.text}")

    # Log response headers
    print(f"Response Headers: {response.headers}")

    # Optionally, you can also log JSON content if the response is in JSON format
    try:
        json_response = response.json()
        print(f"Response JSON: {json_response}")
    except ValueError:
        print("Response is not in JSON format.")

