from flask import Blueprint, render_template, send_from_directory
import os

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def index():
    return send_from_directory("frontend/pages", "index.html")

@pages_bp.route("/dashboard")
def dashboard():
    return send_from_directory("frontend/pages", "dashboard.html")
