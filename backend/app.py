from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Public, no-auth inference endpoint
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilgpt2"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    
    payload = {"inputs": prompt}
    response = requests.post(HUGGINGFACE_API_URL, json=payload)
    
    try:
        result = response.json()
        # Handle response gracefully
        if isinstance(result, list) and "generated_text" in result[0]:
            output = result[0]["generated_text"]
        else:
            output = str(result)
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return jsonify({"message": "Free Hugging Face Demo Running!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
