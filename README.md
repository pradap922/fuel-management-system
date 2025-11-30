# fuel-management-system
# 🚗 Fuel Management System (Flask + SQLite)

A fully offline fuel tracking and vehicle management web application built with **Python Flask** and **SQLite**.

🔹 Track fuel purchases (IN)  
🔹 Issue fuel to vehicles (OUT)  
🔹 Manage driver & vehicle data  
🔹 Real-time fuel stock  
🔹 Generate usage reports

Designed for educational projects, transport companies, depots, bus fleets, and logistics.

---

## ✨ Features

### 🔐 Admin Authentication
- Secure login
- Session-based access
- Fraud prevention

### 📊 Dashboard
- Fuel Stock Summary
- Total Fuel IN / OUT
- Recent transactions

### 🚗 Vehicle Management
- Add vehicles
- Add driver details
- Central vehicle list

### ⛽ Fuel IN
- Record fuel purchased
- Increase stock

### 🛢 Fuel OUT
- Assign fuel to specific vehicle
- Decrease stock

### 📑 Reports
- Filter by date range
- Accountability reports

---

## 🧠 Why SQLite?
✔ Portable  
✔ No server setup  
✔ Works offline  
✔ Very fast  
✔ No installation required

---

# 🛠 Tech Stack

**Backend**
- Python 3 + Flask

**Database**
- SQLite

**Frontend**
- HTML
- CSS (Dark Neon UI)
- JavaScript

---

## 🗂 Project Structure


fuel_management/
│
├── app.py # Main application
├── create_db.py # Initialize database (Run once)
├── database.db # SQLite database file
├── requirements.txt # Dependencies
│
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── main.js
│
└── templates/
├── base.html
├── login.html
├── dashboard.html
├── vehicles.html
├── fuel_in.html
├── fuel_out.html
├── report.html
