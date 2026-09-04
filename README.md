# Hackcult
A full-stack web application built with Python Flask, HTML, and CSS for Origin
# UniSync 🎓

### One Campus. One Source of Truth.

**UniSync** is an Integrated Student Management System designed to bring essential college operations into one unified platform.

Colleges often manage admissions, attendance, fees, examinations, and student records using disconnected spreadsheets and legacy systems. This can lead to duplicate data, inconsistencies, manual reconciliation, and delays in accessing important student information.

UniSync aims to solve this problem by providing a **centralized, role-based student management platform** where administrators, faculty, and students can access the information they need from a single system.

---

## 🚀 Features

### 👨‍🎓 Student Management

* Centralized student records
* University ID-based student identification
* Student profile management
* Student 360° view
* Easy access to academic information

### 📅 Attendance Management

* Record student attendance
* View attendance history
* Subject-wise attendance tracking
* Identify students with low attendance

### 💰 Fee Management

* Track total fees
* Track paid fees
* Identify pending payments
* Student-wise fee information

### 📊 Examination & Results

* Store examination marks
* Subject-wise results
* Student performance tracking
* Academic performance overview

### 🔐 Role-Based Access

UniSync is designed to support different user roles:

* **Admin** – Manage students, fees, attendance, results, and reports
* **Faculty** – Manage attendance and academic records
* **Student** – View personal attendance, fees, and results

### ⚠️ Student Risk / Early Warning

UniSync can use rule-based indicators to identify students who may require attention.

Example factors:

* Low attendance
* Pending fees
* Low academic performance

This helps administrators and faculty identify students who may need support earlier.

### 📈 Dashboard & Analytics

The planned dashboard provides:

* Total students
* Attendance overview
* Fee collection status
* Academic performance
* Student risk indicators
* Important actions and alerts

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* SQLite

### Data

* Mockaroo JSON
* SQLite database

### Frontend

* React *(planned / in development)*

### Development Tools

* VS Code
* Git
* GitHub

---

## 🏗️ Current Project Structure

```text
unisync/
│
├── app.py
├── import_data.py
├── data.json
├── unisync.db
└── README.md
```

### File Description

| File             | Purpose                           |
| ---------------- | --------------------------------- |
| `app.py`         | Flask backend and API             |
| `import_data.py` | Imports Mockaroo data into SQLite |
| `data.json`      | Mockaroo-generated user data      |
| `unisync.db`     | SQLite database                   |
| `README.md`      | Project documentation             |

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/unisync.git
```

Move into the project directory:

```bash
cd unisync
```

---

### 2. Install Flask

Make sure Python is installed.

Then install Flask:

```bash
pip install flask
```

---

### 3. Add Mockaroo Data

Place your Mockaroo JSON file in the project directory and name it:

```text
data.json
```

The current dataset contains university IDs and login-related data.

---

### 4. Import the Data

Run:

```bash
python import_data.py
```

You should see:

```text
Mockaroo data imported successfully!
```

This creates/populates the SQLite database.

---

### 5. Start the Flask Server

Run:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### Home

```http
GET /
```

Returns the backend status.

Example response:

```json
{
  "message": "Welcome to UniSync",
  "status": "Backend is running"
}
```

---

### Get Users

```http
GET /api/users
```

Returns the imported university user IDs.

Passwords are **not returned by the API**.

---

## 🗄️ Database

UniSync currently uses **SQLite** to keep the project simple and beginner-friendly.

### Users Table

```text
users
├── id
├── university_id
└── password
```

> For a production deployment, passwords should be stored using secure password hashing rather than plaintext storage.

---

## 🔄 Planned System Flow

```text
             ┌───────────────┐
             │     Login     │
             └───────┬───────┘
                     │
                     ▼
            ┌─────────────────┐
            │ Role Validation │
            └────────┬────────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Admin      Faculty     Student
          │          │          │
          └──────────┼──────────┘
                     ▼
             ┌───────────────┐
             │   UniSync     │
             │   Dashboard   │
             └───────┬───────┘
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
  Attendance       Fees         Results
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              ┌─────────────┐
              │ Student 360 │
              └─────────────┘
```

---

## 🎯 Problem We Solve

Traditional college management often involves multiple disconnected systems:

```text
Admissions ──┐
Attendance ──┤
Fees ────────┼──► Disconnected Data
Exams ───────┤
Students ────┘
```

This can result in:

* Duplicate records
* Data mismatches
* Manual reconciliation
* Delayed reporting
* Difficulty tracking individual students
* Limited visibility across departments

UniSync brings these areas together:

```text
Students
    │
    ├── Attendance
    │
    ├── Fees
    │
    ├── Results
    │
    └── Risk Indicators
           │
           ▼
      Student 360
           │
           ▼
       Dashboard
```

---

## 🌟 Student 360

One of the core concepts of UniSync is the **Student 360** view.

Instead of checking multiple systems, administrators and authorized faculty can view a student's key information in one place.

Example:

```text
Student
│
├── Personal Information
│
├── Attendance
│
├── Fees
│
├── Examination Results
│
└── Risk / Early Warning
```

This provides a more complete picture of student progress.

---

## 🧠 Early Warning System

UniSync can calculate a simple rule-based risk score.

Example:

```text
Low Attendance       → +40
Pending Fees         → +20
Low Average Marks    → +40
```

Possible classification:

```text
0–29    → LOW
30–59   → MEDIUM
60–100  → HIGH
```

This is a **rule-based early warning system**, not a machine-learning model.

---

## 👥 Team

### Team UniSync

* **Tanmay** – Frontend & UI/UX
* **Abhay** – Backend, Database & APIs
* **Atharva** – Data, Analytics, Report 

---

## 🏆 Hackathon Goal

UniSync is being developed as a practical solution for modernizing student administration in colleges.

The goal is to create a system that is:

* Simple to use
* Centralized
* Scalable
* Data-driven
* Role-based
* Easy to demonstrate
* Useful for administrators, faculty, and students

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] React frontend
* [ ] Admin dashboard
* [ ] Faculty dashboard
* [ ] Student dashboard
* [ ] Secure login
* [ ] Password hashing
* [ ] Role-based authentication
* [ ] Student 360 interface
* [ ] Attendance management UI
* [ ] Fee management UI
* [ ] Examination/result management
* [ ] Analytics and charts
* [ ] PDF reports
* [ ] Excel exports
* [ ] Notifications
* [ ] Global student search
* [ ] Advanced early-warning analytics
* [ ] Cloud deployment

---

## 📌 Project Status

**Current Status:** 🚧 Under Development

The current prototype includes:

* Flask backend
* SQLite database
* Mockaroo data import
* User API
* Basic backend health endpoint

More modules and the frontend are being developed as part of the hackathon project.

---

## 📄 License

This project is developed for educational and hackathon purposes.

---

# UniSync

### One Campus. One Source of Truth. 🎓

