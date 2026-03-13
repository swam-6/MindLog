import joblib
import os
from backend.models.db import MoodLog

MODEL_PATH = os.path.join(os.path.dirname(__file__), "mood_model.pkl")
_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_mood(text: str) -> str:
    model = get_model()
    label = model.predict([text])[0]
    return label

def check_alert_pattern(user_id: int) -> bool:
    """Return True if user has 3+ consecutive Depressed/Anxious entries in last 7."""
    recent = (MoodLog.query
              .filter_by(user_id=user_id)
              .order_by(MoodLog.created_at.desc())
              .limit(7)
              .all())
    if len(recent) < 3:
        return False
    concern = {"Depressed", "Anxious"}
    streak = 0
    for log in recent:
        if log.predicted_label in concern:
            streak += 1
            if streak >= 3:
                return True
        else:
            streak = 0
    return False
