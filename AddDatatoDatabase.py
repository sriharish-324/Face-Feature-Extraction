import json
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
"7376211CS320":
        {
            "name": "Thiru",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        },
"7376212CT119":
        {
            "name": "Jashwanth R",
            "major": "CT",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Status": "Marked"
        },
"7376212CT108":
        {
            "name": "Chandru M",
            "major": "CT",
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
with open('student_data.json', 'w') as json_file:
    json.dump(data, json_file)
