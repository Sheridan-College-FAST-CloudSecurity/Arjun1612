from flask import Flask  # Import Flask

app = Flask(__name__)  # Initialize Flask app

@app.route('/')
def hello():
    return "Hello, Arjun Singh"

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for easier troubleshooting
