from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

app = Flask(__name__)

VERIFY_TOKEN = "VERIFY_TOKEN_key"
ACCESS_TOKEN = "ACCESS_TOKEN_key"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verify webhook
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Invalid token', 403

    elif request.method == 'POST':
        data = request.get_json()
        # Process messages here
        return 'OK', 200

if __name__ == '__main__':
    app.run()

