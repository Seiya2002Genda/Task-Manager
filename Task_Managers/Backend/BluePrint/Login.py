from flask import Blueprint, render_template, request, redirect, session, url_for
from Task_Managers.Backend.ConnectDatabase import ConnectDatabase

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = ConnectDatabase().connect()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user and user["password"] == password:
            session["user_id"] = user["id"]
            return redirect(url_for("task.manage_task"))

        return "Login Failed"

    return render_template("Login.html")