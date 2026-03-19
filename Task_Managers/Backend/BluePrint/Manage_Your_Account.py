from flask import Blueprint, render_template, session
from Task_Managers.Backend.ConnectDatabase import ConnectDatabase

account_bp = Blueprint("account", __name__)

@account_bp.route("/account")
def manage_account():
    db = ConnectDatabase().connect()
    cursor = db.cursor(dictionary=True)

    user_id = session.get("user_id")

    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()

    return render_template("Manage_Your_Account.html", user=user)