from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user
from models.user import db, User, bcrypt
from views.auth import auth_bp
from views.dashboard import dashboard_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi Database & Login Manager
db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprint
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

@app.route("/")
def home():
    return render_template("index.html", user=current_user)

# Buat database saat pertama kali
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
