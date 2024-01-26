import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# Firebase Credentials
cred = credentials.Certificate(".venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://attendanceproject-bbd6f-default-rtdb.firebaseio.com/', 'storageBucket': 'attendanceproject-bbd6f.appspot.com'})

folderPathImages = 'images'
listPathImages = os.listdir(folderPathImages)
imgListImages = []

# Extracting the student ID from each picture
studentIDs = []


for path in listPathImages:
    imgListImages.append(cv2.imread(os.path.join(folderPathImages, path)))
    studentIDs.append(os.path.splitext(path)[0])

    fileName = f'{folderPathImages}/{path}'

    bucket = storage.bucket()

    blob = bucket.blob(fileName)

    blob.upload_from_filename(fileName)

# Printing the amount of elements stored into imgListImages to ensure we have done it correctly
print(len(imgListImages))


def generateEncodings(images):

    # Initialize the list of encodings
    encodingsList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]

        encodingsList.append(encode)

    return encodingsList


encodingListKnown = generateEncodings(imgListImages)
encodingsListwithIDs = [encodingListKnown, studentIDs]

encodingsFile = open("EncodingsFile.p", "wb")

pickle.dump(encodingsListwithIDs, encodingsFile)

encodingsFile.close()
