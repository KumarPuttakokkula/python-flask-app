from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route("/")
def root():
    return "You have accessed the root this website. <br>To access the Info, reach out: /app/v1/info</br> <br>To access health of this website: /app/v1/helathz</br>"

@app.route("/app/v1/info")
def details():
    return jsonify({
        "message": "You've developed and deployed this Python Flask App from ArgoCD !!",
        "hostname": socket.gethostname(),
        "time": datetime.datetime.now().strftime("%I:%M:%S%p on %B %d %Y"),
        "deployed_on": "Kubernetes",
        "deployed_by": "Kumar Puttakokkula"
    })

@app.route("/app/v1/healthz")
def health():
    return jsonify({"status": "up"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")