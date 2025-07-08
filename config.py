
MONGO_URI = "mongodb://localhost:27017/"
DB_AUTH = "TA_BHK"
COLLECTION_STUDENS = "student"
COLLECTION_TEACHER = "teacher"
COLLECTION_WORKER = "worker"
COLLECTION_USER = "user"
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

class API_IP_INFO:
    IPINFO_API_KEY = '2fe8c03a0d4bfe'

# class API_FIREBASE:
# # API TO FIREBASE
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred,{
#         'databaseURL' : 'https://facerecognition-f0072-default-rtdb .firebaseio.com/',
#         'storageBucket' : 'facerecognition-f0072.appspot.com'
#     })
