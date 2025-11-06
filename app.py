from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "App vulnerable de ejemplo"

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # Vulnerabilidad intencional: ejecuta comando con entrada del usuario
    os.system(f"ping -n 1 {host}")
    return f"Ping a {host} ejecutado"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
