# Task Managers 2

A full-stack task management web application built with **Flask + MySQL**, featuring OTP authentication, deadline tracking, and progress visualization.

---

## 🚀 Overview

Task Managers 2 is a productivity-focused web application that allows users to:

* Create and manage tasks
* Set deadlines for each task
* Track progress visually with a progress bar
* Securely authenticate using OTP (One-Time Password)

This project demonstrates full-stack development including backend logic, database design, and frontend UI/UX.

---

## 🧠 Key Features

### 🔐 Authentication System

* Email-based login & signup
* OTP (One-Time Password) verification
* Password hashing for security

### ✅ Task Management

* Create tasks with deadlines
* Mark tasks as completed or pending
* Delete tasks
* Search tasks dynamically

### 📊 Progress Tracking

* Adjustable progress (0–100%)
* Dynamic progress bar visualization
* Auto-update status (pending → done)

### ⏱ Deadline System

* Set due date for each task
* Sort tasks by urgency

---

## 🛠 Tech Stack

### Backend

* Python (Flask)
* MySQL (mysql-connector)
* Flask-Mail (OTP email system)

### Frontend

* HTML5
* CSS3 (Custom UI)
* JavaScript (Vanilla JS)

### Security

* Werkzeug (password hashing)
* Session-based authentication

---

## 📂 Project Structure

```
Task_Managers_2/
│
├── Backend/
│   ├── BluePrint/
│   │   ├── Login.py
│   │   ├── Signup.py
│   │   ├── ManageTask.py
│   │   └── ...
│   │
│   ├── Database/
│   │   ├── ConnectDatabase.py
│   │   └── CreateDatabase.py
│   │
│   ├── Verification.py
│   └── Config.py
│
├── FrontEnd/
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── ManageTask.html
│   │   └── ...
│   │
│   └── static/
│       ├── css/
│       └── js/
│
├── app.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/task-managers-2.git
cd task-managers-2
```

---

### 2. Install Dependencies

```
pip install flask mysql-connector-python flask-mail werkzeug
```

---

### 3. Configure Environment

Edit `Config.py`:

```
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_DATABASE = "task_manager"

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "your_email@gmail.com"
MAIL_PASSWORD = "your_app_password"

OTP_EXPIRE_SECONDS = 300
```

---

### 4. Run Application

```
python app.py
```

Access:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

(Add screenshots here if needed)

---

## 🔥 Future Improvements

* REST API (JSON + fetch)
* React frontend
* JWT authentication
* Task reminders (email / notification)
* Calendar integration
* AI-based task recommendations

---

## 📌 Learning Outcomes

This project demonstrates:

* Full-stack web development
* Database schema design
* Authentication & security implementation
* UI/UX design with dynamic interaction
* Debugging real-world issues

---

## 👤 Author

Seiya Genda
Computer Science × Marketing Student
Aspiring Data Scientist / Full-Stack Engineer

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
****
