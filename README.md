# 🚀 Student Management System (Flask CRUD + Authentication)

This project is a **Student Management System** built using **Flask** and **SQLite** as part of my internship (Task 3).

It includes secure authentication and full CRUD functionality, along with a modern SaaS-style dashboard UI.

---

## ✨ Features

🔐 Authentication
- User Registration & Login
- Password hashing using Werkzeug
- Session-based access control

📊 Dashboard
- Personalized welcome page
- Total students count
- Quick navigation

📋 Student Management (CRUD)
- ➕ Add Students
- 📄 View Students
- ✏️ Edit Students
- 🗑️ Delete Students

---

## 🔐 Security Features

- Protected routes (only accessible after login)
- Redirects unauthorized users to login page
- Passwords are securely hashed (no plain text storage)
- Session-based authentication maintained across pages

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- SQLite 🗄️
- HTML & CSS 🎨

---

## 📁 Project Structure
python-fullstack-task3/
│
├── app.py
├── database.db
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── students.html
│ ├── add_student.html
│ └── edit_student.html
│
├── static/
│ └── style.css
│
├── screenshots/
│ ├── dashboard.png
│ ├── students.png
│ ├── login.png
│ └── register.png

## ⚙️ Installation & Setup

1. Clone the repository:

git clone https://github.com/Tappyyokka/User-management-with-CRUD.git                    


2. Navigate into the folder:

cd your-repo-name


3. Install dependencies:

pip install flask


4. Run the application:

python app.py


5. Open in browser:

http://127.0.0.1:5000


---

## 📸 Screenshots

### 🏠 Dashboard
![Dashboard](screenshots/dashboard.png)

### 📋 Students Page
![Students](screenshots/students.png)

### 🔐 Login Page
![Login](screenshots/login.png)

### 📝 Register Page
![Register](screenshots/register.png)

---

## 📚 What I Learned

- Building a full CRUD system using Flask
- Implementing authentication and session management
- Working with SQLite database
- Designing a clean and structured UI
- Connecting backend logic with frontend templates

---

## 🚀 Future Improvements

- 🔍 Search & filter students
- ⚠️ Delete confirmation popup
- 📱 Mobile responsiveness
- 🌙 Dark mode
- 📊 Charts & analytics on dashboard

---

## 🙌 Acknowledgment

This project was built as part of my internship learning journey.

---

## 📬 Connect with me

Feel free to connect or share feedback!
