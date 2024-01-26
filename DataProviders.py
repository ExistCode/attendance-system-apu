import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(".venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://attendanceproject-bbd6f-default-rtdb.firebaseio.com/'})

ref = db.reference("Students")

data = {
    "TP011111": {
        "name": "Xin Weng Yan",
        "major": "CS (DS)",
        "starting_year": 2022,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
    "TP012345": {
        "name": "Jong Kook",
        "major": "CS (DS)",
        "starting_year": 2022,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
    "TP054321": {
        "name": "Lim Chuan",
        "major": "CS (DS)",
        "starting_year": 2022,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
    "TP063338": {
        "name": "Lex Luthor",
        "major": "CS (DS)",
        "starting_year": 2022,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
    "TP068713": {
        "name": "Hohoho",
        "major": "CS (DS)",
        "starting_year": 2022,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
    "TP088888": {
        "name": "Boboho",
        "major": "CS (DS)",
        "starting_year": 2022,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
}

for key, value in data.items():
    ref.child(key).set(value)
