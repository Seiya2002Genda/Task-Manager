from flask import Blueprint, render_template, redirect, url_for, flash, session
from Task_Managers_2.Backend.ConnectDatabase import ConnectDatabase

account_bp = Blueprint("account", __name__)


@account_bp.route("/account")
def manage_account():
    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect(url_for("login.login"))

    db = ConnectDatabase().connect()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            u.id,
            u.email,
            u.created_at,
            COUNT(t.id) AS total_tasks,
            SUM(CASE WHEN t.status='pending' THEN 1 ELSE 0 END) AS pending_tasks,
            SUM(CASE WHEN t.status='done' THEN 1 ELSE 0 END) AS done_tasks
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        WHERE u.id=%s
        GROUP BY u.id, u.email, u.created_at
        """,
        (session["user_id"],)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template("Manage_Your_Account.html", user=user)