from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.db import db, MoodLog
from backend.ml.predictor import predict_mood, check_alert_pattern

mood_bp = Blueprint("mood", __name__)

@mood_bp.route("/log", methods=["POST"])
@jwt_required()
def log_mood():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    text = data.get("text", "").strip()
    score = data.get("mood_score")

    if not text:
        return jsonify({"error": "Journal entry cannot be empty"}), 400
    if score is None or not (1 <= int(score) <= 10):
        return jsonify({"error": "Mood score must be between 1 and 10"}), 400

    label = predict_mood(text)
    alert = check_alert_pattern(user_id)

    entry = MoodLog(
        user_id=user_id,
        entry_text=text,
        mood_score=int(score),
        predicted_label=label,
        alert_flag=alert
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({
        "message": "Mood logged successfully",
        "entry": entry.to_dict(),
        "alert": alert
    }), 201

@mood_bp.route("/history", methods=["GET"])
@jwt_required()
def get_history():
    user_id = int(get_jwt_identity())
    limit = request.args.get("limit", 30, type=int)
    logs = (MoodLog.query
            .filter_by(user_id=user_id)
            .order_by(MoodLog.created_at.desc())
            .limit(limit)
            .all())
    return jsonify({"logs": [l.to_dict() for l in logs]}), 200

@mood_bp.route("/stats", methods=["GET"])
@jwt_required()
def get_stats():
    user_id = int(get_jwt_identity())
    logs = MoodLog.query.filter_by(user_id=user_id).all()

    if not logs:
        return jsonify({"total": 0, "average_score": 0, "label_counts": {}, "alert_active": False}), 200

    total = len(logs)
    avg_score = round(sum(l.mood_score for l in logs) / total, 1)
    label_counts = {}
    for l in logs:
        label_counts[l.predicted_label] = label_counts.get(l.predicted_label, 0) + 1
    alert_active = check_alert_pattern(user_id)

    return jsonify({
        "total": total,
        "average_score": avg_score,
        "label_counts": label_counts,
        "alert_active": alert_active
    }), 200

@mood_bp.route("/delete/<int:log_id>", methods=["DELETE"])
@jwt_required()
def delete_log(log_id):
    user_id = int(get_jwt_identity())
    log = MoodLog.query.filter_by(id=log_id, user_id=user_id).first()
    if not log:
        return jsonify({"error": "Log not found"}), 404
    db.session.delete(log)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200
