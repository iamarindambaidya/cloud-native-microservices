from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/login")
def login():
    return jsonify({"message": "Login successful", "token": "dummy-token"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)