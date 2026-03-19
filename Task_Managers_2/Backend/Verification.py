import random
import time
from flask_mail import Mail, Message
from flask import current_app

mail = Mail()


class Verification:
    @staticmethod
    def generate_otp():
        return f"{random.randint(100000, 999999)}"

    @staticmethod
    def generate_expire_time():
        return int(time.time()) + int(current_app.config["OTP_EXPIRE_SECONDS"])

    @staticmethod
    def is_expired(expire_at: int):
        return int(time.time()) > int(expire_at)

    @staticmethod
    def send_otp(email: str, otp: str):
        msg = Message(
            subject="Task Manager OTP Verification",
            recipients=[email]
        )
        msg.body = (
            f"Your OTP code is: {otp}\n\n"
            f"This code will expire in {current_app.config['OTP_EXPIRE_SECONDS'] // 60} minutes."
        )
        mail.send(msg)