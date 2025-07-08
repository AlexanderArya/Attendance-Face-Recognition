import cv2
import face_recognition
import pickle
import os
import config

# Importing student images
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in PathList:
    img = cv2.imread(os.path.join(folderPath, path))
    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])

    # Membuat file bernama path dengan uruan yang sama dengan lokal komputer
    fileName = f'{folderPath}/{path}'
    # Membuat koneksi ke Firebase Cloud Storage
    bucket = config.storage.bucket()
    # Membuat objek yang merepresentasikan file yang akan dikirim ke Firebase
    blob = bucket.blob(fileName)
    # Mengnggah isi file dari komputer lokal ke dalam Firebase maka terdapat variable (Upload)
    blob.upload_from_filename(fileName)


encodeListKnown = []
for img in imgList:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        encode = face_recognition.face_encodings(img)[0]
        encodeListKnown.append(encode)
    except IndexError:
        print("No face detected in one of the images.")

print("Encoding Complete")

# Creating and writing to a binary file
with open("EncodeFile.p", "wb") as file:
    encodeListKnownWithIds = [encodeListKnown, studentIds]
    pickle.dump(encodeListKnownWithIds, file)

print("File saved")


