from flask import Blueprint
from controllers.dashboard_controller import dashboard

dashboard_bp = Blueprint("dashboard", __name__)

dashboard_bp.route("/dashboard")(dashboard)
