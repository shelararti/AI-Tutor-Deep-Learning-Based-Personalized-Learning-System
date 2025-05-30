# 🤖 AI Tutor – Personalized Learning System

An interactive Streamlit-based AI tutor designed to personalize learning paths using quizzes, mastery prediction, convex optimization, and AI-driven topic recommendations.

---

## 🚀 Features

- 🧠 **AI-Powered Q&A**: Ask subject-related questions and get beginner-friendly responses.
- 📝 **Auto-Generated Quizzes**: Pulls quizzes from a MySQL database based on topic and level.
- 📊 **Mastery Score Prediction**: Uses sentence embeddings to predict understanding.
- ⏱️ **Convex Optimization**: Allocates study hours efficiently based on skill level and topic difficulty.
- 🎯 **Topic Recommendations**: Suggests what to study next based on prerequisites and mastery.
- 💾 **Progress Tracking**: Saves and loads student data via JSON files.

---

## 📦 Installation

git clone https://github.com/yourusername/ai-tutor.git
cd ai-tutor
pip install -r requirements.txt
streamlit run main.py

---

## ⚠️ WARNING: g4f Usage
This project uses g4f to call language models like GPT-4 without API keys.

---

## ❗ Please note:
- g4f is not an official OpenAI library.

- It reverse-engineers public endpoints and may break without warning.

- It can violate OpenAI’s terms of service.

- Never use it in production or with sensitive/personal data.

To avoid risk, switch to the official OpenAI API like this:

import openai

openai.api_key = "YOUR_API_KEY"
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[{"role": "user", "content": prompt}]
)
Use g4f only if you're okay with the risks. You’ve been warned.

---

🔧 Configuration
Update your MySQL credentials in quiz_generator.py.

Ensure student_data.json is writable and located in the root directory.

Populate your MySQL database (quiz_db) with initial quiz data.

---

## 📁 File Structure

ai-tutor/
├── main.py                   # Streamlit UI
├── tutor_backend.py          # Progress logic & prerequisites
├── quiz_generator.py         # Quiz DB access & AI Q&A
├── convex_optimizer.py       # Convex optimization logic
├── mastery_predictor.py      # Embedding-based mastery scoring
├── recommendation_ui.py      # Recommendation UI
├── student_data.json         # Stores per-user topic scores
├── requirements.txt          # Python dependencies
└── README.md                 # You're reading it!

---

## 🧠 Topics Covered
Subjects: Data Science, Computer Science, Mathematics
Examples: MySQL, DSA, Pandas, NumPy, Power BI, EDA
Algorithms, OS, Networking
Calculus, Linear Algebra, Probability

---

## 🤝 Contributing
Pull Requests are welcome!
Open an issue for new features, bug fixes, or enhancements.

---

## 📜 License
This project is for educational and personal use only.
Please do not use g4f or this system in production unless you fully understand the legal and ethical implications.

---

## 📬 Contact
Questions or suggestions?
DM me or raise a GitHub issue.

