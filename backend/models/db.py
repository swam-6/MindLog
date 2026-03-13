from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    logs = db.relationship("MoodLog", backref="user", lazy=True)

class MoodLog(db.Model):
    __tablename__ = "mood_logs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    entry_text = db.Column(db.Text, nullable=False)
    mood_score = db.Column(db.Integer, nullable=False)   # 1-10 rating from user
    predicted_label = db.Column(db.String(20), nullable=False)
    alert_flag = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "entry_text": self.entry_text,
            "mood_score": self.mood_score,
            "predicted_label": self.predicted_label,
            "alert_flag": self.alert_flag,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M")
        }
