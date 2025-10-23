import os
import time
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Retrieve Contentful credentials from environment variables
CONTENTFUL_SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
CONTENTFUL_ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

# Validate that the required environment variables are set
if not CONTENTFUL_SPACE_ID or not CONTENTFUL_ACCESS_TOKEN:
    raise ValueError("Contentful credentials are not set in environment variables.")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    # Simulate processing time
    time.sleep(2)
    output = f"Processed prompt: {prompt}"

    # Fetch content from Contentful
    content = fetch_content_from_contentful()

    return jsonify({"output": output, "content": content})

def fetch_content_from_contentful():
    url = f"https://cdn.contentful.com/spaces/{CONTENTFUL_SPACE_ID}/entries"
    headers = {
        "Authorization": f"Bearer {CONTENTFUL_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch content"}

@app.route('/')
def home():
    return jsonify({"message": "Contentful Integration Running!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
