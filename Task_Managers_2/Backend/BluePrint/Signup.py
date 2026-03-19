from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from mysql.connector import IntegrityError
from Task_Managers_2.Backend.ConnectDatabase import ConnectDatabase

signup_bp = Blueprint("signup", __name__)


@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()

        if not email or not password or not confirm_password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("signup.signup"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("signup.signup"))

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return redirect(url_for("signup.signup"))

        hashed_password = generate_password_hash(password)

        db = ConnectDatabase().connect()
        cursor = db.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (%s, %s)",
                (email, hashed_password)
            )
            db.commit()
            flash("Account created successfully. Please login.", "success")
            return redirect(url_for("login.login"))

        except IntegrityError:
            flash("This email is already registered.", "error")
            return redirect(url_for("signup.signup"))

        finally:
            cursor.close()
            db.close()

    return render_template("Signup.html")