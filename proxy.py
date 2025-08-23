from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # 🔑 allow CORS for all domains

AIPIPE_URL = "https://aipipe.org/openrouter/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        api_key = data.get("apiKey")
        email = data.get("email")
        payload = data.get("payload")

        if not api_key:
            return jsonify({"error": "API key is required"}), 400

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-User-Email": email
        }

        r = requests.post(AIPIPE_URL, headers=headers, json=payload, timeout=30)
        return jsonify(r.json()), r.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# if __name__ == "__main__":
#     from pyngrok import ngrok
#     import uvicorn
#     port = int(os.environ.get("PORT", 8000))
#     # Your reserved ngrok domain here
#     reserved_domain = "still-finch-sacred.ngrok-free.app"
#     # Open an ngrok tunnel with reserved domain
#     public_url = ngrok.connect(addr=port, hostname=reserved_domain)
#     print(f"ngrok tunnel available at: {public_url.public_url}")

#     uvicorn.run(app, host="0.0.0.0", port=port)