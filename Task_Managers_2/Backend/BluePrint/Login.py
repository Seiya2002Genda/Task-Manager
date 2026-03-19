from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from Task_Managers_2.Backend.ConnectDatabase import ConnectDatabase

login_bp = Blueprint("login", __name__)


@login_bp.route("/")
def index():
    if session.get("user_id"):
        return redirect(url_for("task.manage_task"))
    return render_template("index.html")


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("task.manage_task"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not email or not password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("login.login"))

        db = ConnectDatabase().connect()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        cursor.close()
        db.close()

        if not user:
            flash("Email not found.", "error")
            return redirect(url_for("login.login"))

        if not check_password_hash(user["password"], password):
            flash("Incorrect password.", "error")
            return redirect(url_for("login.login"))

        session["user_id"] = user["id"]
        session["user_email"] = user["email"]

        flash("Login successful.", "success")
        return redirect(url_for("task.manage_task"))

    return render_template("Login.html")


@login_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login.login"))