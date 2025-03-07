# Sets up the modules to connect the backend to the frontend
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)  # Create a Flask app
CORS(app)  # Allows frontend to talk to backend

# Create an endpoint that accepts POST requests, like a landing pad for requests
@app.route('/process', methods=['POST'])
def process():
    data = request.json  # Get data sent from frontend
    word = data.get("word", "")  # Extract 'word' from JSON
    
    # Create a response message
    response_message = f"You sent the word: {word.upper()}!"

    return jsonify({"message": response_message})  # Send response as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Start Flask server
