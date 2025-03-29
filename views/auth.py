from flask import Blueprint
from controllers.auth_controller import register, login, logout

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/register", methods=["GET", "POST"])(register)
auth_bp.route("/login", methods=["GET", "POST"])(login)
auth_bp.route("/logout")(logout)
