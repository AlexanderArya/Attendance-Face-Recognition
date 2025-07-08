from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import requests
from functools import wraps

gateway = Flask(__name__)
gateway.config["SECRET_KEY"] = "iniadalahsecretkeyku"

AUTH_SERVICE_URL = "http://localhost:5011"
DASHBOARD_SERVICE_URL = "http://localhost:5012"
ABSENSI_SERVICE_URL = "http://localhost:5013"

# Masuk web
@gateway.route("/")
def login_page():
    return render_template('init.html')

@gateway.route("/register")
def register():
    return render_template('register.html')

@gateway.route("/auth/<action>", methods=['POST'])
def handle_auth(action):
    data = request.json
    print(data)
    
    try:
        if action == 'login':
            print("Masuk ke login")
            response = requests.post(f"{AUTH_SERVICE_URL}/login", json=data)
            return jsonify(response.json()), response.status_code

        elif action == 'register':
            print("Masuk ke register")
            response = requests.post(f"{AUTH_SERVICE_URL}/register", json=data)
            print(response.json())
            return jsonify(response.json()), response.status_code

        else:
            return jsonify({"error": "Aksi tidak dikenali"}), 400

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Gagal menghubungi layanan auth", "details": str(e)}), 500


@gateway.route("/absen")
def absen():
    return render_template('absen.html')

if __name__ == "__main__":
    gateway.run(debug=True, port=5010)
