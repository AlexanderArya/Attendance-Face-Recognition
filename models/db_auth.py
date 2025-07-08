from flask import jsonify
from pymongo import MongoClient
import config
import pickle
# import cv2, face_recognition
import numpy as np

class Database_Autentifikasi:
    def __init__(self):
        try:
            self.client = MongoClient(config.MONGO_URI)
            self.db = self.client[config.DB_AUTH]
            self.user_collection = self.db[config.COLLECTION_USER]
            self.teacher_collection = self.db[config.COLLECTION_TEACHER]
        except Exception as e:
            print(f"Error koneksi ke database: {e}")

    def insertDataTeacher(self, nama, NUPTK, NIP, jabatan, role):
        print("sudah masuk sini hkamsldfh")
        if not self.db:
            print("⚠️ Database tidak tersedia!")
            return {"error": "Database tidak tersedia"}
        try:
            return self.teacher_collection.insert_one({"nama": nama,"NUPTK": NUPTK,"NIP": NIP,"jabatan": jabatan,"role": role})
        except NotImplementedError:
            print("⚠️ NotImplementedError terjadi di insertDataTeacher")
            return {"error": "Fungsi belum diimplementasikan"}
        except Exception as e:
            print(f"❌ Terjadi error: {e}")
            return {"error": "Gagal menyimpan data", "detail": str(e)}
