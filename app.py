from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "fuel_secret"

def db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# 🔐 LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['username']
        pwd = request.form['password']
        conn = db()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (name, pwd)).fetchone()
        if user:
            session["user"] = name
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# 🏠 Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = db()

    total_in = conn.execute(
        "SELECT IFNULL(SUM(litres),0) FROM fuel_transactions WHERE type='IN'"
    ).fetchone()[0] or 0

    total_out = conn.execute(
        "SELECT IFNULL(SUM(litres),0) FROM fuel_transactions WHERE type='OUT'"
    ).fetchone()[0] or 0

    stock = total_in - total_out

    recent = conn.execute("""
        SELECT ft.*, v.vehicle_no
        FROM fuel_transactions ft
        LEFT JOIN vehicles v ON ft.vehicle_id = v.id
        ORDER BY created_at DESC
        LIMIT 5
    """).fetchall()

    return render_template(
        "dashboard.html",
        total_in=total_in,
        total_out=total_out,
        stock=stock,
        recent=recent
    )


# 🚗 Vehicles
@app.route("/vehicles", methods=["GET", "POST"])
def vehicles():
    if "user" not in session:
        return redirect("/")

    conn = db()

    if request.method == "POST":
        conn.execute("INSERT INTO vehicles(vehicle_no, driver) VALUES(?,?)",
                     (request.form['vehicle_no'], request.form['driver']))
        conn.commit()

    rows = conn.execute("SELECT * FROM vehicles").fetchall()
    return render_template("vehicles.html", rows=rows)


# 🟢 Fuel IN
@app.route("/fuel-in", methods=["GET", "POST"])
def fuel_in():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        conn = db()
        conn.execute("""
            INSERT INTO fuel_transactions(date, vehicle_id, fuel, litres, type, remarks)
            VALUES (?, NULL, ?, ?, 'IN', ?)
        """, (request.form['date'], request.form['fuel'], request.form['litres'], request.form['remarks']))
        conn.commit()
        return redirect("/dashboard")

    return render_template("fuel_in.html")


# 🔴 Fuel OUT
@app.route("/fuel-out", methods=["GET", "POST"])
def fuel_out():
    if "user" not in session:
        return redirect("/")

    conn = db()
    vehicles = conn.execute("SELECT * FROM vehicles").fetchall()

    if request.method == "POST":
        conn.execute("""
            INSERT INTO fuel_transactions(date, vehicle_id, fuel, litres, type, remarks)
            VALUES (?, ?, ?, ?, 'OUT', ?)
        """, (request.form['date'], request.form['vehicle'], request.form['fuel'], request.form['litres'], request.form['remarks']))
        conn.commit()
        return redirect("/dashboard")

    return render_template("fuel_out.html", vehicles=vehicles)


# 📊 Reports
@app.route("/report")
def report():
    if "user" not in session:
        return redirect("/")

    f = request.args.get("from", "2024-01-01")
    t = request.args.get("to", datetime.now().strftime("%Y-%m-%d"))

    conn = db()
    data = conn.execute("""
        SELECT ft.*, v.vehicle_no
        FROM fuel_transactions ft
        LEFT JOIN vehicles v ON ft.vehicle_id = v.id
        WHERE ft.date BETWEEN ? AND ?
    """, (f, t)).fetchall()

    return render_template("report.html", data=data, f=f, t=t)


if __name__ == "__main__":
    app.run(debug=True)
