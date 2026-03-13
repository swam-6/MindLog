import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.models.db import db

def create_app():
    app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/pages")
    
    app.config["SECRET_KEY"] = "moodtracker-secret-2024"
    app.config["JWT_SECRET_KEY"] = "jwt-mood-secret-2024"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///moodtracker.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)
    JWTManager(app)
    db.init_app(app)

    from backend.routes.auth import auth_bp
    from backend.routes.mood import mood_bp
    from backend.routes.pages import pages_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(mood_bp, url_prefix="/api/mood")
    app.register_blueprint(pages_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
