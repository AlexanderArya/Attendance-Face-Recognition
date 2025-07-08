import sys
import os
from flask import Flask, render_template, request, session, url_for, redirect, flash, jsonify
from models.db_auth import Database_Autentifikasi

# Menginisialisai authentification Flask
authentification = Flask(__name__)
authentification.config["SECRET_KEY"] = "iniadalahsecretkeyku"

# Memasukan class di dalam db_auth ke dalam service
user_db = Database_Autentifikasi()


@authentification.route('/register', methods=['POST'])
def register():
    data = request.json
    print("sudah masuk ke controller")
    if not data:
        return jsonify({"error": "Data tidak boleh kosong"}), 400

    try:
        result = user_db.insertDataTeacher(
            data.get('nama'),
            data.get('NUPTK'),
            data.get('NIP'),
            data.get('jabatan'),
            data.get('role')
        )
        print(result)
        return result
    except Exception as e:
        return jsonify({"error": "Terjadi kesalahan sistem", "detail": str(e)}), 500

    
# Contoh penggunaan model di dalam route
@authentification.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Username dan password diperlukan"}), 400

    # Gunakan model untuk autentikasi
    user = user_db.authenticate(data["username"], data["password"])
    if user:
        session["user"] = user
        return jsonify({"message": "Login berhasil", "user": user}), 200
    else:
        return jsonify({"error": "Username atau password salah"}), 401

if __name__ == "__main__":
    authentification.run(debug=True, port=5011)


