from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "fuel_management_secret_key"

# =========================
# CONFIG: LOGIN CONTROL
# =========================
ALLOWED_GMAILS = [
    "mithiran@gmail.com",
    "admin@gmail.com",
    "projectfuel@gmail.com"
]

FIXED_PASSWORD = "Fuel@123"
FUEL_PRICES = {
    "Petrol": 105,
    "Diesel": 95,
    "Oil": 180
}

# =========================
# DATABASE CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# =========================
# FUEL SUMMARY (PETROL / DIESEL / OIL)
# =========================
def fuel_summary():
    conn = get_db()
    fuels = ["Petrol", "Diesel", "Oil"]
    summary = {}

    for f in fuels:
        fuel_in = conn.execute(
            "SELECT IFNULL(SUM(litres),0) FROM fuel_transactions WHERE type='IN' AND fuel=?",
            (f,)
        ).fetchone()[0]

        fuel_out = conn.execute(
            "SELECT IFNULL(SUM(litres),0) FROM fuel_transactions WHERE type='OUT' AND fuel=?",
            (f,)
        ).fetchone()[0]

        summary[f] = {
            "in": fuel_in,
            "out": fuel_out,
            "stock": fuel_in - fuel_out
        }

    return summary

# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("home.html")

# =========================
# LOGIN (GMAIL STYLE - OFFLINE)
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not email.endswith("@gmail.com"):
            message = "Only Gmail accounts are allowed"

        elif email not in ALLOWED_GMAILS:
            message = "This Gmail ID is not authorized"

        elif password != FIXED_PASSWORD:
            message = "Incorrect password"

        else:
            conn = get_db()
            user = conn.execute(
                "SELECT * FROM users WHERE username=?",
                (email,)
            ).fetchone()

            if not user:
                conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (email, password)
                )
                conn.commit()

            session["user"] = email
            return redirect("/dashboard")

    return render_template("login.html", message=message)

# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# =========================
# DASHBOARD (FUEL-WISE)
# =========================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    # Fuel summary (already exists if you added earlier)
    summary = fuel_summary()

    # 🔥 NEW: Recent Fuel OUT records
    recent_out = conn.execute("""
        SELECT ft.date, ft.fuel, ft.litres, v.vehicle_no
        FROM fuel_transactions ft
        JOIN vehicles v ON ft.vehicle_id = v.id
        WHERE ft.type = 'OUT'
        ORDER BY ft.date DESC
        LIMIT 5
    """).fetchall()

    return render_template(
        "dashboard.html",
        summary=summary,
        recent_out=recent_out
    )

# =========================
# VEHICLE MANAGEMENT
# =========================
@app.route("/vehicles", methods=["GET", "POST"])
def vehicles():
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    if request.method == "POST":
        conn.execute(
            "INSERT INTO vehicles (vehicle_no, driver) VALUES (?, ?)",
            (request.form["vehicle_no"], request.form["driver"])
        )
        conn.commit()

    rows = conn.execute("SELECT * FROM vehicles").fetchall()
    return render_template("vehicles.html", rows=rows)

# =========================
# FUEL IN (SEPARATE PETROL / DIESEL / OIL)
# =========================
@app.route("/fuel-in", methods=["GET", "POST"])
def fuel_in():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        conn = get_db()
        conn.execute("""
            INSERT INTO fuel_transactions (date, fuel, litres, type, remarks)
            VALUES (?, ?, ?, 'IN', '')
        """, (
            request.form["date"],
            request.form["fuel"],
            request.form["litres"]
        ))
        conn.commit()
        return redirect("/fuel-in")

    summary = fuel_summary()
    return render_template("fuel_in.html", summary=summary)

# =========================
# FUEL OUT (SEPARATE PETROL / DIESEL / OIL)
# =========================
@app.route("/fuel-out", methods=["GET", "POST"])
def fuel_out():
    if "user" not in session:
        return redirect("/login")

    conn = get_db()
    vehicles = conn.execute("SELECT * FROM vehicles").fetchall()

    if request.method == "POST":
        conn.execute("""
            INSERT INTO fuel_transactions
            (date, vehicle_id, fuel, litres, type, remarks)
            VALUES (?, ?, ?, ?, 'OUT', '')
        """, (
            request.form["date"],
            request.form["vehicle"],
            request.form["fuel"],
            request.form["litres"]
        ))
        conn.commit()
        return redirect("/fuel-out")

    summary = fuel_summary()
    return render_template(
        "fuel_out.html",
        vehicles=vehicles,
        summary=summary
    )

# =========================
# REPORTS
# =========================
@app.route("/report")
def report():
    if "user" not in session:
        return redirect("/login")

    f = request.args.get("from", "2024-01-01")
    t = request.args.get("to", datetime.now().strftime("%Y-%m-%d"))

    conn = get_db()
    data = conn.execute("""
        SELECT ft.*, v.vehicle_no
        FROM fuel_transactions ft
        LEFT JOIN vehicles v ON ft.vehicle_id = v.id
        WHERE ft.date BETWEEN ? AND ?
        ORDER BY ft.date DESC
    """, (f, t)).fetchall()

    return render_template("report.html", data=data, f=f, t=t)
@app.route("/edit-vehicle/<int:id>", methods=["GET","POST"])
def edit_vehicle(id):
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    if request.method == "POST":
        conn.execute(
            "UPDATE vehicles SET vehicle_no=?, driver=? WHERE id=?",
            (
                request.form["vehicle_no"],
                request.form["driver"],
                id
            )
        )
        conn.commit()
        return redirect("/vehicles")

    vehicle = conn.execute(
        "SELECT * FROM vehicles WHERE id=?", (id,)
    ).fetchone()

    return render_template("edit_vehicle.html", vehicle=vehicle)
@app.route("/edit-fuel/<int:id>", methods=["GET","POST"])
def edit_fuel(id):
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    if request.method == "POST":
        conn.execute("""
            UPDATE fuel_transactions
            SET date=?, litres=?, remarks=?
            WHERE id=?
        """, (
            request.form["date"],
            request.form["litres"],
            request.form["remarks"],
            id
        ))
        conn.commit()
        return redirect("/report")

    fuel = conn.execute(
        "SELECT * FROM fuel_transactions WHERE id=?", (id,)
    ).fetchone()

    return render_template("edit_fuel.html", fuel=fuel)
@app.route("/delete-vehicle/<int:id>")
def delete_vehicle(id):
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    # 1️⃣ Delete all fuel records related to this vehicle
    conn.execute(
        "DELETE FROM fuel_transactions WHERE vehicle_id=?",
        (id,)
    )

    # 2️⃣ Delete the vehicle
    conn.execute(
        "DELETE FROM vehicles WHERE id=?",
        (id,)
    )

    conn.commit()

    return redirect("/vehicles")
@app.route("/bill/<int:id>")
def bill(id):
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    record = conn.execute("""
        SELECT ft.*, v.vehicle_no
        FROM fuel_transactions ft
        LEFT JOIN vehicles v ON ft.vehicle_id = v.id
        WHERE ft.id=?
    """, (id,)).fetchone()

    if not record:
        return "Bill not found"

    price = FUEL_PRICES.get(record["fuel"], 0)
    total = price * record["litres"]

    return render_template(
        "bill.html",
        r=record,
        price=price,
        total=total
    )

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)
