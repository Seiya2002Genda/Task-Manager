from flask import Blueprint, render_template, request, redirect, url_for
from Task_Managers.Backend.ConnectDatabase import ConnectDatabase

signup_bp = Blueprint("signup", __name__)

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = ConnectDatabase().connect()
        cursor = db.cursor()

        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        db.commit()

        return redirect(url_for("login.login"))

    return render_template("Signup.html")