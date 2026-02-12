# Fuel-Management-System
A modern, offline Fuel Management System built using Python Flask, SQLite, HTML, CSS, and JavaScript.  This system digitally manages fuel stock, vehicle fuel usage, billing, and dashboard analytics with a professional petroleum-style interface.

📌 Project Overview

The Fuel Management System is designed to replace manual fuel logbooks with a digital solution.
It allows administrators to manage:

Fuel IN (Stock addition)

Fuel OUT (Vehicle fuel issuance)

Vehicle management

Fuel stock tracking

Bill generation

Dashboard analytics

Vehicle-wise fuel usage charts

Fully offline and suitable for college projects and small fleet operations.



🛠️ Technology Stack
🔹 Frontend

HTML5

CSS3 (Neon Dark UI)

JavaScript

Chart.js (for dashboard graphs)

🔹 Backend

Python

Flask

🔹 Database

SQLite (Offline Database)

📂 Project Structure
fuel_management/
│
├── app.py
├── database.db
├── requirements.txt
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   ├── petrol.png
│   │   ├── diesel.png
│   │   ├── oil.png
│   │   └── bharat_petroleum.png
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── vehicles.html
│   ├── edit_vehicle.html
│   ├── fuel_in.html
│   ├── fuel_out.html
│   ├── report.html
│   ├── edit_fuel.html
│   ├── bill.html
│
└── README.md

🔐 Features
✅ Admin Login (Offline Gmail Simulation)

Only fixed Gmail IDs allowed

Fixed password authentication

Secure session-based login

✅ Fuel Management

Petrol

Diesel

Oil

Separate stock tracking

Real-time stock updates

✅ Vehicle Management

Add vehicle

Edit vehicle

Delete vehicle (with cascade delete)

✅ Fuel Transactions

Record Fuel IN

Record Fuel OUT

Edit records

Filter by date

✅ Bill Generation

Automatic bill calculation

Price per litre defined in backend

Printable bill format

✅ Dashboard

Fuel stock summary cards

Recent Fuel OUT transactions

Vehicle-wise fuel usage chart

Real-time data updates

📊 Dashboard Analytics

Fuel IN / OUT summary

Current stock per fuel type

Vehicle-wise fuel consumption bar chart

Print bill directly from dashboard

🧮 Billing Logic

Fuel prices defined in backend:

FUEL_PRICES = {
    "Petrol": 105,
    "Diesel": 95,
    "Oil": 180
}


Total = Litres × Price per litre

Bills can be printed directly from system.

💻 Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/yourusername/fuel-management-system.git
cd fuel-management-system

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run the Application
python app.py


Open browser:

http://127.0.0.1:5000

📦 Requirements.txt
Flask

🗄️ Database

SQLite database (database.db)

Automatically created if not exists

Fully offline operation

🎓 Academic Use

This project demonstrates:

CRUD operations

Session management

Relational database handling

Dashboard analytics

Billing system

Data visualization

Responsive UI design

🚀 Future Enhancements

GST calculation

Role-based access

PDF bill download

Monthly reports

Low stock alerts

Export to Excel

Mobile compatibility

📜 License

This project is developed for educational purposes.

⭐ Why This Project Is Strong

Full CRUD functionality

Dashboard analytics

Billing system

Chart integration

Clean UI

Offline capability

Industry-style logic
