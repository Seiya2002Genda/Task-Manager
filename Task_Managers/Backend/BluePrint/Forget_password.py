from flask import Blueprint, render_template, request, session, redirect, url_for
from Task_Managers.Backend.Verification import Verification
from Task_Managers.Backend.ConnectDatabase import ConnectDatabase
from flask import current_app

forget_bp = Blueprint("forget", __name__)

verifier = Verification()

# =========================
# STEP 1: EMAIL入力 → OTP送信
# =========================
@forget_bp.route("/forget", methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email = request.form["email"]

        otp = verifier.generate_otp()

        # sessionに保存
        session["reset_email"] = email
        session["otp"] = otp

        # メール送信
        verifier.send_otp(current_app, email, otp)

        return redirect(url_for("forget.verify"))

    return render_template("forget_password.html")


# =========================
# STEP 2: OTP確認
# =========================
@forget_bp.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        user_otp = request.form["otp"]

        if user_otp == session.get("otp"):
            return redirect(url_for("forget.reset_password"))
        else:
            return "Invalid OTP"

    return render_template("verify.html")


# =========================
# STEP 3: パスワード再設定
# =========================
@forget_bp.route("/reset", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        new_password = request.form["password"]
        email = session.get("reset_email")

        db = ConnectDatabase().connect()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE users SET password=%s WHERE email=%s",
            (new_password, email)
        )
        db.commit()

        # session削除
        session.pop("otp", None)
        session.pop("reset_email", None)

        return redirect(url_for("login.login"))

    return render_template("reset_password.html")