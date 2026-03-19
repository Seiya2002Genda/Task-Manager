from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from Task_Managers_2.Backend.ConnectDatabase import ConnectDatabase
from Task_Managers_2.Backend.Verification import Verification

forget_bp = Blueprint("forget", __name__)


@forget_bp.route("/forget", methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()

        if not email:
            flash("Please enter your email.", "error")
            return redirect(url_for("forget.forget"))

        db = ConnectDatabase().connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT id, email FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if not user:
            flash("No account found with that email.", "error")
            return redirect(url_for("forget.forget"))

        otp = Verification.generate_otp()
        expire_at = Verification.generate_expire_time()

        session["reset_email"] = email
        session["otp"] = otp
        session["otp_expire_at"] = expire_at

        Verification.send_otp(email, otp)

        flash("OTP has been sent to your email.", "success")
        return redirect(url_for("forget.verify"))

    return render_template("forget_password.html")


@forget_bp.route("/verify", methods=["GET", "POST"])
def verify():
    if "otp" not in session or "reset_email" not in session:
        flash("Please request a new OTP.", "error")
        return redirect(url_for("forget.forget"))

    if request.method == "POST":
        user_otp = request.form.get("otp", "").strip()

        if not user_otp:
            flash("Please enter the OTP.", "error")
            return redirect(url_for("forget.verify"))

        if Verification.is_expired(session.get("otp_expire_at", 0)):
            session.pop("otp", None)
            session.pop("otp_expire_at", None)
            flash("OTP has expired. Please request a new one.", "error")
            return redirect(url_for("forget.forget"))

        if user_otp != session.get("otp"):
            flash("Invalid OTP.", "error")
            return redirect(url_for("forget.verify"))

        session["otp_verified"] = True
        flash("OTP verified successfully.", "success")
        return redirect(url_for("forget.reset_password"))

    return render_template("verify.html")


@forget_bp.route("/reset", methods=["GET", "POST"])
def reset_password():
    if not session.get("otp_verified") or "reset_email" not in session:
        flash("Unauthorized password reset request.", "error")
        return redirect(url_for("forget.forget"))

    if request.method == "POST":
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()

        if not password or not confirm_password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("forget.reset_password"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("forget.reset_password"))

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return redirect(url_for("forget.reset_password"))

        hashed_password = generate_password_hash(password)

        db = ConnectDatabase().connect()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE users SET password=%s WHERE email=%s",
            (hashed_password, session["reset_email"])
        )
        db.commit()

        cursor.close()
        db.close()

        session.pop("otp", None)
        session.pop("otp_expire_at", None)
        session.pop("otp_verified", None)
        session.pop("reset_email", None)

        flash("Password reset successful. Please login.", "success")
        return redirect(url_for("login.login"))

    return render_template("reset_password.html")