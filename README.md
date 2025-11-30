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

1️⃣ Download & Extract Project

Download the project folder (ZIP or Git clone)

Extract it

Open it in VS Code / Terminal

2️⃣ Install Python

📥 Download: https://www.python.org/downloads/

➡️ During install → CHECK this box:
✔️ Add Python to PATH

3️⃣ Install Required Packages

Open terminal inside the project folder:

pip install flask


OR

pip install -r requirements.txt

4️⃣ Create the Database (Run Only Once)

Run this:

python create_db.py


This will generate:

database.db


✔️ Your system now has tables:

users

vehicles

fuel_transactions

5️⃣ Start the Application
python app.py


If it runs successfully, you will see:

 * Running on http://127.0.0.1:5000

6️⃣ Open in Browser

Paste this URL into your browser:

http://127.0.0.1:5000

🔑 Login Credentials (Default)
Username: admin
Password: admin123

7️⃣ Use the System
📌 Available pages:

Dashboard → Fuel summary

Vehicles → Add vehicles & drivers

Fuel IN → Record purchases

Fuel OUT → Issue fuel to vehicles

Report → Date-wise fuel transactions

🔁 Restarting the App

If you close CMD / app, you do not need to run database again.

Just run:

python app.py

🛑 Do Not Run Again (Only once)

🚫 Do NOT run create_db.py every time
Only if:

You deleted the database

You want a fresh system
