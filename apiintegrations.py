import requests
from dotenv import load_dotenv
import os
from Models.UserResponseModel import UsersResponse

#load environment variables from .env file
load_dotenv()

# Get the base URL from the environment variable
base_url = os.getenv('BASE_URL')

def call_getendpoint():
    # Define the endpoint you want to call
    endpoint = '/users'
    # Construct the full URL
    url = f"{base_url}{endpoint}"
    try:
        # Make the GET request
        response = requests.get(url)
        return response
    except Exception as e:
        return {"error": str(e)}

def executeendpoint():
    result = call_getendpoint()
    print(result.status_code)
    if result.status_code == 200:
        users_response = UsersResponse.model_validate_json(result.text)
        for user in users_response.users:
            print(user.id)
            print(user.firstName)
            print(user.lastName)
    else:
        print({"error": f"Request failed with status code {result.status_code}"})

def call_postendpoint():
    # Define the endpoint you want to call
    endpoint = '/users/add'
    # Construct the full URL
    url = f"{base_url}{endpoint}"
    # Define the payload for the POST request
    payload = {
        "firstName": "John",
        "lastName": "Doe",
        "age": 30
    }
    try:
        # Make the POST request
        
        response = requests.post(url, json=payload)
        print(response.content)
    except Exception as e:
        print({"error": str(e)})
    
if __name__ == "__main__":
    call_postendpoint()