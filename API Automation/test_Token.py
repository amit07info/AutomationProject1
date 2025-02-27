import requests
from requests.auth import HTTPBasicAuth

# Define API credentials (example)
username = "admin"  # Your username
password = "password123"  # Your password

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

# Authentication header (using HTTPBasicAuth)
auth = HTTPBasicAuth(username, password)

# Define the endpoint for fetching token (if applicable)
token_endpoint = f"{BASE_URL}/auth"

# Make the request to the auth endpoint
response = requests.post(token_endpoint, auth=auth)

# Check if the request was successful and extract the token
if response.status_code == 200:
    token_data = response.json()
    token = token_data.get('token')  # Assuming the token is in 'token' field
    print(f"Fetched Token: {token}")
else:
    print(f"Failed to fetch token. Status Code: {response.status_code}, Response: {response.text}")

# Define login credentials
username = "your_username"
password = "your_password"

# Authentication endpoint to get the JWT token
login_url = "https://api.example.com/login"

# Prepare data (e.g., credentials)
data = {
    "username": username,
    "password": password
}

# Make a POST request to get the JWT token
response = requests.post(login_url, json=data)

# If successful, extract the JWT token
if response.status_code == 200:
    token_data = response.json()
    jwt_token = token_data.get('token')
 print(f"JWT Token: {jwt_token}")
else:
    print(f"Failed to fetch JWT token. Status Code: {response.status_code}, Response: {response.text}")
