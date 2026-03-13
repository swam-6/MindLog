# 🌿 MindLog — AI-Powered Mental Health Tracker

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-orange?style=flat-square&logo=scikit-learn)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![SDG](https://img.shields.io/badge/UN%20SDG-3.4%20Mental%20Health-4C9A2A?style=flat-square)

> A full-stack web application that uses Natural Language Processing and Machine Learning to analyse daily mood journal entries, detect emotional patterns, and alert users to concerning mental health trends — aligned with **United Nations Sustainable Development Goal 3.4**.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [SDG Alignment](#-un-sdg-alignment)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [API Reference](#-api-reference)
- [ML Model](#-ml-model)
- [Future Scope](#-future-scope)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 Overview

MindLog addresses a critical gap in mental health awareness — **75% of people with mental health conditions receive no treatment**, primarily due to stigma, cost, and lack of early detection. MindLog provides a private, stigma-free journaling platform where an AI model analyses the emotional content of daily entries in real time, classifying mood states and flagging patterns of distress before they escalate to clinical severity.

The system uses a **dual-input design**: users provide a self-rated mood score (1–10) alongside a free-text journal entry. The ML model independently analyses the text and assigns an emotion label. When the two diverge — for example, a user rates themselves 7/10 but writes with anxious language — the gap itself becomes a clinically significant signal of underreported distress.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **JWT Authentication** | Secure register/login with bcrypt password hashing and JWT token protection |
| ✍️ **Mood Journal** | Free-text daily entries with a 1–10 self-rating slider |
| 🤖 **AI Mood Classification** | SVM model classifies entries into Positive, Neutral, Anxious, or Depressed |
| 📈 **Trend Visualisation** | Interactive line chart showing mood score history over the last 14 days |
| 📊 **Label Breakdown** | Visual bar breakdown of emotion distribution across all entries |
| ⚠️ **Smart Alert System** | Automatically flags when 3+ consecutive entries indicate distress |
| 🆘 **Resource Links** | Alert banner provides direct links to verified mental health helplines |
| 🗃️ **Entry History** | Scrollable log of all past entries with delete functionality |
| 📱 **Responsive UI** | Clean, accessible interface that works on desktop and mobile |

---

## 🌍 UN SDG Alignment

This project directly contributes to **[UN Sustainable Development Goal 3 — Good Health and Well-Being](https://sdgs.un.org/goals/goal3)**.

| SDG Target | Contribution |
|---|---|
| **3.4** — Reduce mental health mortality & morbidity | AI-driven early detection of distress patterns before clinical intervention is required |
| **3.5** — Prevent substance abuse & mental disorders | Daily journaling and self-monitoring reduces unhealthy coping behaviours |
| **3.8** — Universal access to health services | Free web access with no cost barrier; links users to verified helplines and therapy resources |

> **Primary alignment: SDG 3.4**
>
> *"By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment, and promote mental health and well-being."*

---

## 🛠 Tech Stack

### Backend
- **Python 3.11** — Core language
- **Flask 3.0** — Web framework and REST API
- **Flask-JWT-Extended** — JSON Web Token authentication
- **Flask-SQLAlchemy** — ORM for database management
- **SQLite** — Lightweight relational database (upgradeable to PostgreSQL)
- **Werkzeug** — Password hashing (bcrypt)

### Machine Learning
- **scikit-learn 1.5.2** — SVM classifier and TF-IDF vectoriser
- **joblib** — Model serialisation and loading

### Frontend
- **HTML5 / CSS3 / Vanilla JavaScript** — No framework dependency
- **Chart.js 4.4** — Interactive mood trend visualisation
- **Google Fonts** — DM Serif Display + DM Sans typography

---

## 📁 Project Structure

```
moodtracker/
│
├── app.py                          # Flask application factory & entry point
├── train_model.py                  # ML training script (run once before startup)
├── requirements.txt                # Python dependencies
├── README.md
│
├── backend/
│   ├── models/
│   │   └── db.py                   # SQLAlchemy models: User, MoodLog
│   │
│   ├── routes/
│   │   ├── auth.py                 # POST /api/auth/register, /api/auth/login
│   │   ├── mood.py                 # POST /api/mood/log, GET /history, /stats, DELETE
│   │   └── pages.py                # Serves HTML pages
│   │
│   └── ml/
│       ├── predictor.py            # Model loading, prediction, alert pattern detection
│       └── mood_model.pkl          # Trained SVM model (auto-generated by train_model.py)
│
└── frontend/
    └── pages/
        ├── index.html              # Login / Register page
        └── dashboard.html          # Main application dashboard
```

---

## ⚙️ Installation

### Prerequisites
- Python **3.11** (recommended — all packages have pre-built wheels)
- pip

### Step 1 — Clone the repository
```bash
git clone https://github.com/your-username/mindlog-mental-health-tracker.git
cd mindlog-mental-health-tracker
```

### Step 2 — Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3.11 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Train the ML model
```bash
python train_model.py
```
This generates `backend/ml/mood_model.pkl`. A classification report will appear in the terminal confirming success.

### Step 5 — Run the application
```bash
python app.py
```

### Step 6 — Open in browser
```
http://localhost:5000
```

---

## 📡 API Reference

All protected routes require the header:
```
Authorization: Bearer <JWT_TOKEN>
```

### Authentication

| Method | Endpoint | Auth | Request Body | Response |
|--------|----------|------|--------------|----------|
| `POST` | `/api/auth/register` | None | `{ name, email, password }` | `{ token, user }` |
| `POST` | `/api/auth/login` | None | `{ email, password }` | `{ token, user }` |

### Mood

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/api/mood/log` | JWT | Submit a mood entry; returns AI label and alert flag |
| `GET` | `/api/mood/history` | JWT | Fetch last 30 entries (use `?limit=N` to customise) |
| `GET` | `/api/mood/stats` | JWT | Summary stats: total, average score, label counts, alert status |
| `DELETE` | `/api/mood/delete/:id` | JWT | Delete a specific log entry by ID |

### Example — Log a mood entry

**Request:**
```json
POST /api/mood/log
{
  "text": "Feeling very anxious about my exams, can't stop overthinking everything",
  "mood_score": 3
}
```

**Response:**
```json
{
  "message": "Mood logged successfully",
  "entry": {
    "id": 12,
    "entry_text": "Feeling very anxious about my exams...",
    "mood_score": 3,
    "predicted_label": "Anxious",
    "alert_flag": false,
    "created_at": "2024-11-15 14:32"
  },
  "alert": false
}
```

---

## 🤖 ML Model

### Algorithm
**Support Vector Machine (SVM)** with a linear kernel, wrapped in a scikit-learn `Pipeline` with TF-IDF vectorisation.

### Pipeline
```
Raw Text → TF-IDF Vectoriser (3000 features, 1-gram + 2-gram) → SVM Classifier → Label
```

### Output Labels

| Label | Description | UI Colour |
|---|---|---|
| **Positive** | Confident, happy, grateful language | 🟢 Green |
| **Neutral** | Stable, unremarkable language | ⚪ Grey |
| **Anxious** | Worry, stress, panic, overthinking language | 🟠 Orange |
| **Depressed** | Hopelessness, emptiness, withdrawal language | 🟣 Purple |

### Alert Logic
The pattern detector checks the **7 most recent entries** per user. If **3 or more consecutive entries** are labelled Anxious or Depressed, the `alert_flag` is set to `True` and the dashboard displays a banner with verified helpline links.

### Training Data
120 synthetic journal entries (30 per class). For production, replace with validated clinical datasets such as **DASS-21 (Depression Anxiety Stress Scales)**.

---

## 🔮 Future Scope

1. **Expand training data** — Integrate DASS-21 survey responses for higher clinical accuracy
2. **Weekly insights email** — Automated mood summary report delivered every Sunday
3. **Voice input** — Speech-to-text journaling via the Web Speech API
4. **Therapist referral module** — Connect high-risk users to verified mental health professionals
5. **Multi-language support** — Hindi, Tamil, Malayalam for broader regional accessibility
6. **Mobile application** — Flutter-based cross-platform mobile app
7. **Explainability (XAI)** — Show users which words drove the AI classification using LIME/SHAP

---

## 🆘 Mental Health Resources (India)

| Organisation | Contact | Website |
|---|---|---|
| iCall | 9152987821 | [icallhelpline.org](https://icallhelpline.org) |
| Vandrevala Foundation | 1860-2662-345 (24/7) | [vandrevalafoundation.com](https://vandrevalafoundation.com) |
| NIMHANS | — | [nimhans.ac.in](https://nimhans.ac.in) |
| The Live Love Laugh Foundation | — | [thelivelovelaughfoundation.org](https://www.thelivelovelaughfoundation.org) |

---



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

*"Early detection saves lives. MindLog exists to catch the signal before it becomes a crisis."*
