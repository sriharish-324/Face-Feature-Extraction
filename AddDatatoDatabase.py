import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("faceattendancerealtime-8dce7-firebase-adminsdk-y90l2-08a1fb47f5.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-8dce7-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "7376221CS314":
        {
            "name": "SriSivaRam",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        },
    "7376221CS280":
        {
            "name": "Rithik",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        },
    "7376211CS299":
        {
                "name": "Sriharish ",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        },
    "7376211EC328":
        {
                "name": "Yuvaraj N ",
            "major": "ECE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        },
    "7376212CT119":
        {
            "name": "Jashwanth R ",
            "major": "CT",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        }
}

for key, value in data.items():
    ref.child(key).set(value)