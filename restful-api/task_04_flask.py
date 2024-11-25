from flask import Flask, jsonify, request
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Set up logging
logging.basicConfig(
    filename='api.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per minute"]
)

@app.before_request
def log_request():
    logging.info(f"Request: {request.method} {request.url}")

@app.after_request
def log_response(response):
    logging.info(f"Response: {response.status}")
    return response

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded"}), 429
