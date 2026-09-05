from flask import Flask, request, jsonify
from flask_cors import CORS

from database import get_db, create_tables

app = Flask(__name__)
CORS(app)

create_tables()


@app.route("/student/login", methods=["POST"])
def student_login():

    data = request.get_json()

    student_id = data.get("id")
    password = data.get("password")

    if not student_id or not password:
        return jsonify({
            "success": False,
            "message": "ID and password are required"
        }), 400

    conn = get_db()

    student = conn.execute("""
        SELECT * FROM students
        WHERE student_id = ?
    """, (student_id,)).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "success": False,
            "message": "Invalid ID or password"
        }), 401

    if student["password"] != password:
        return jsonify({
            "success": False,
            "message": "Invalid ID or password"
        }), 401

    return jsonify({
        "success": True,
        "message": "Login successful"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
    
from flask import Flask, jsonify, request, session, redirect, url_for
from flask_cors import CORS
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for sessions
CORS(app, supports_credentials=True)     # Enables CORS with cookie support

# ----------------------------------------------------
# 1. MOCK DATABASE (30 Students with Login Credentials)
# ----------------------------------------------------
first_names = ["Arjun", "Priya", "Rahul", "Sneha", "Karan", "Aarav", "Ananya", "Rohan", "Isha", "Vikram",
               "Neha", "Aditya", "Pooja", "Siddharth", "Kavya", "Rishabh", "Tanvi", "Kabir", "Meera", "Yash"]
last_names = ["Singh", "Mehta", "Verma", "Patel", "Nair", "Sharma", "Gupta", "Joshi", "Chopra", "Reddy"]

random.seed(42)  # Generates consistent data

STUDENTS_DB = {}

# Student 1 (Logged-in default match)
STUDENTS_DB["CS2024001"] = {
    "roll_no": "01",
    "student_id": "CS2024001",
    "password": "password123",
    "name": "Arjun Singh",
    "department": "Computer Science",
    "semester": "5",
    "attendance_percentage": 91.2,
    "attended_classes": 94,
    "total_classes": 103,
    "cgpa": 8.4,
    "cgpa_remark": "Excellent",
    "rank": 3,
    "fee_status": "Paid",
    "fee_remark": "All dues cleared",
    "credits_earned": 84,
    "total_credits": 180,
    "attendance_history": {
        "months": ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb"],
        "values": [88, 91, 85, 72, 78, 91, 91.2]
    },
    "upcoming_exams": [
        {"day": "4", "month": "Mar", "subject": "Algorithms", "time": "10:00 AM", "location": "Hall A", "type": "Final"},
        {"day": "6", "month": "Mar", "subject": "Networks", "time": "2:00 PM", "location": "Hall B", "type": "Final"},
        {"day": "8", "month": "Mar", "subject": "DBMS", "time": "10:00 AM", "location": "Hall A", "type": "Final"}
    ]
}

# Remaining 29 Students
for i in range(2, 31):
    roll_str = f"{i:02d}"
    student_id = f"CS2024{i:03d}"
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    att_percentage = random.randint(55, 98)
    
    STUDENTS_DB[student_id] = {
        "roll_no": roll_str,
        "student_id": student_id,
        "password": "password123",
        "name": full_name,
        "department": "Computer Science",
        "semester": "5",
        "attendance_percentage": att_percentage,
        "attended_classes": int((att_percentage / 100) * 100),
        "total_classes": 100,
        "cgpa": round(random.uniform(6.5, 9.5), 1),
        "cgpa_remark": "Good" if att_percentage > 75 else "Needs Improvement",
        "rank": i,
        "fee_status": "Paid" if i % 3 != 0 else "Pending",
        "fee_remark": "All dues cleared" if i % 3 != 0 else "Pending Semester Fee",
        "credits_earned": random.randint(70, 90),
        "total_credits": 180,
        "attendance_history": {
            "months": ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb"],
            "values": [random.randint(60, 95) for _ in range(7)]
        },
        "upcoming_exams": [
            {"day": "4", "month": "Mar", "subject": "Algorithms", "time": "10:00 AM", "location": "Hall A", "type": "Final"}
        ]
    }


# ----------------------------------------------------
# 2. AUTHENTICATION ENDPOINTS
# ----------------------------------------------------
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    student_id = data.get('student_id')
    password = data.get('password')

    student = STUDENTS_DB.get(student_id)
    if student and student['password'] == password:
        session['user_id'] = student_id  # Save student ID in session
        return jsonify({"success": True, "message": "Login successful", "student_id": student_id}), 200
    
    return jsonify({"success": False, "message": "Invalid Student ID or Password"}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"success": True, "message": "Logged out"}), 200


# ----------------------------------------------------
# 3. DASHBOARD & ATTENDANCE ENDPOINTS
# ----------------------------------------------------
@app.route('/api/student/dashboard', methods=['GET'])
def get_dashboard_data():
    # Retrieve logged-in student, default to CS2024001 if session is empty
    student_id = session.get('user_id', 'CS2024001')
    student_data = STUDENTS_DB.get(student_id)

    if not student_data:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "student_name": student_data["name"],
        "student_id": student_data["student_id"],
        "department": student_data["department"],
        "semester": student_data["semester"],
        "attendance_percentage": student_data["attendance_percentage"],
        "attended_classes": student_data["attended_classes"],
        "total_classes": student_data["total_classes"],
        "cgpa": student_data["cgpa"],
        "cgpa_remark": student_data["cgpa_remark"],
        "rank": student_data["rank"],
        "total_students": len(STUDENTS_DB),
        "fee_status": student_data["fee_status"],
        "fee_remark": student_data["fee_remark"],
        "credits_earned": student_data["credits_earned"],
        "total_credits": student_data["total_credits"],
        "attendance_history": student_data["attendance_history"],
        "upcoming_exams": student_data["upcoming_exams"]
    })

@app.route('/api/students/attendance', methods=['GET'])
def get_30_students_attendance():
    roster = []
    for sid, student in STUDENTS_DB.items():
        status = "Present" if student["attendance_percentage"] >= 75 else "Absent"
        roster.append({
            "roll_no": student["roll_no"],
            "student_id": student["student_id"],
            "name": student["name"],
            "attendance_percentage": student["attendance_percentage"],
            "status": status
        })
    
    # Sort roster by Roll Number
    roster.sort(key=lambda x: x["roll_no"])
    return jsonify(roster)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 