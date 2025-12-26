import requests
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

url = "http://localhost:7860/api/v1/run/375a7d91-b3ba-482e-8d5a-43914c33facb"

# Get API key from environment
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")

# Request headers with authentication
headers = {
    "Authorization": f"Bearer {LANGFLOW_API_KEY}",
    "Content-Type": "application/json"
}

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "what is the use of integration and derivation in real life?",
    "session_id": str(uuid.uuid4())
}

try:
    # Send API request with headers
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    
    # Parse and print the response
    result = response.json()
    
    # Extract the chat message from the response
    if "outputs" in result:
        for output in result["outputs"]:
            if "outputs" in output:
                for sub_output in output["outputs"]:
                    if "results" in sub_output:
                        message = sub_output["results"].get("message", {})
                        print("Agent Response:")
                        print(message.get("text", ""))
    else:
        print("Full Response:", result)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Response status: {e.response.status_code}")
        print(f"Response body: {e.response.text}")
except ValueError as e:
    print(f"Error parsing response: {e}")