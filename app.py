from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps Project!"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/info")
def info():
    return jsonify({"app": "v1.0", "author": "Your Name"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)