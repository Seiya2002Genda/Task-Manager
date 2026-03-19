import random
from flask_mail import Message, Mail

mail = Mail()

class Verification:

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_otp(self, app, email, otp):
        with app.app_context():
            msg = Message("Your OTP Code",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email])
            msg.body = f"Your OTP is: {otp}"
            mail.send(msg)