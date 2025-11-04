import os
import requests

# Load your Hugging Face token from an environment variable
HF_TOKEN = os.getenv("HF_TOKEN")  # Make sure you set this in your environment
API_URL = "https://api-inference.huggingface.co/models/Abdelaaziz/toxic-darija-bert-classification"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    """
    Sends a POST request to the Hugging Face API and returns the JSON response.
    """
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # raise an error if the request failed
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

def evaluate_response(response):
    """
    Evaluates the API response and returns 0 (valid) or 1 (offensive).
    """
    # Hugging Face API for text classification usually returns a list of dicts
    if isinstance(response, list) and len(response) > 0:
        predictions = response[0]  # get first prediction
        if isinstance(predictions, list):
            # Map scores to labels
            label_scores = {item['label']: item['score'] for item in predictions}
            label_0_score = label_scores.get('LABEL_0', 0)
            label_1_score = label_scores.get('LABEL_1', 0)
            return 0 if label_0_score > label_1_score else 1
        elif isinstance(predictions, dict) and 'label' in predictions:
            return 0 if predictions['label'] == 'LABEL_0' else 1
    print("Unexpected response format:", response)
    return -1  # error case

# Example usage
test_comment = "wa lke7al"
payload = {"inputs": test_comment}

output = query(payload)
result = evaluate_response(output)

if result == 0:
    print("Comment valid ✅")
elif result == 1:
    print("Comment non valid ❌")
else:
    print("Error evaluating the comment")
