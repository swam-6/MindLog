# GitHub Repository Setup Guide

---

## 1. Repository Name
```
mindlog-mental-health-tracker
```

---

## 2. Short Description (max 350 characters — paste this into the "About" box on GitHub)

```
AI-powered mental health journaling web app built with Flask + scikit-learn. Uses NLP (TF-IDF + SVM) to classify daily mood entries as Positive, Neutral, Anxious, or Depressed. Detects distress patterns and alerts users with helpline resources. Aligned with UN SDG 3.4.
```

---

## 3. Topics / Tags (add these in the GitHub Topics field)

```
mental-health
flask
python
machine-learning
nlp
scikit-learn
svm
tfidf
jwt-authentication
sqlite
sdg
un-sdg
healthcare
web-application
mood-tracker
sentiment-analysis
student-project
2-credits
html-css-javascript
chartjs
```

---

## 4. Website Field
```
http://localhost:5000
```
(Update this if you deploy to a cloud platform like Render or Railway)

---

## 5. Social Preview Description
For the repository's Open Graph / social card description (Settings → Social Preview):

```
MindLog detects early signs of mental distress using AI — a Flask + scikit-learn web app
aligned with UN SDG 3.4. Built as a 2-credit academic project.
```

---

## 6. First Pinned Comment / Discussion Post

Post this as your first GitHub Discussion or pinned issue:

---

### About This Project

**MindLog** was developed as a 2-credit academic project at [Your College Name], Department of Computer Science and Information Technology.

**Project Guide:** [Supervisor Name]
**Academic Year:** 2024–25
**UN SDG Alignment:** SDG 3 — Good Health and Well-Being (Target 3.4)

The project demonstrates the practical application of:
- Natural Language Processing (TF-IDF vectorisation)
- Supervised Machine Learning (Support Vector Machine)
- RESTful API design with Flask
- JWT-based authentication
- Full-stack web development without a frontend framework

**Key insight:** The dual-input design (user self-rating + AI text analysis) was deliberately chosen to detect the gap between how users *think* they feel and what their language *actually* reveals — a well-documented phenomenon in mental health research known as affective forecasting bias.

---

## 7. README Badges Reference

Copy-paste these badges at the top of your README:

```markdown
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-orange?style=flat-square&logo=scikit-learn)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![SDG](https://img.shields.io/badge/UN%20SDG-3.4%20Mental%20Health-4C9A2A?style=flat-square)
```

---

## 8. How to Push to GitHub (step by step)

```bash
# Inside your project folder
git init
git add .
git commit -m "Initial commit: MindLog AI Mental Health Tracker"

# Create a new repo on github.com first, then:
git remote add origin https://github.com/YOUR-USERNAME/mindlog-mental-health-tracker.git
git branch -M main
git push -u origin main
```

> Tip: Add a `.gitignore` to exclude the database and model file:

```
# .gitignore
instance/
*.db
backend/ml/mood_model.pkl
__pycache__/
*.pyc
venv/
.env
```

> Note: Since `mood_model.pkl` is excluded, anyone who clones your repo must run `python train_model.py` first — mention this in your README (already included).
