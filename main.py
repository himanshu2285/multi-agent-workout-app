import requests
import os
import uuid
from dotenv import load_dotenv
load_dotenv()

url = "http://localhost:7860/api/v1/run/375a7d91-b3ba-482e-8d5a-43914c33facb"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Give me a 5 day workout plan for building muscle. My body weight is 60kg"
}
payload["session_id"] = str(uuid.uuid4())



try:
    # Send API request
    # response = requests.request("POST", url, json=payload, headers=headers)
    response = requests.request("POST", url, json=payload)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")