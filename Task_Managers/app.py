from flask import Flask
from flask_mail import Mail

from Backend.BluePrint.Login import login_bp
from Backend.BluePrint.Signup import signup_bp
from Backend.BluePrint.Forget_password import forget_bp
from Backend.BluePrint.ManageTask import task_bp
from Backend.BluePrint.Manage_Your_Account import account_bp

from Backend.Config import Config
from Backend.CreateDatabase import CreateDatabase
from Backend.Verification import mail

app = Flask(__name__,
            template_folder="FrontEnd/templates",
            static_folder="FrontEnd/static")

app.config.from_object(Config)

# Mail init
mail.init_app(app)

# DB init
CreateDatabase().create_tables()

# Blueprints
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(forget_bp)
app.register_blueprint(task_bp)
app.register_blueprint(account_bp)

if __name__ == "__main__":
    app.run(debug=True)