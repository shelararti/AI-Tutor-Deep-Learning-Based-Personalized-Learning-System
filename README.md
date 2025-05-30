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

```bash
git clone https://github.com/yourusername/ai-tutor.git
cd ai-tutor
pip install -r requirements.txt
streamlit run main.py
⚠️ WARNING: g4f Usage
This project uses g4f to call language models like GPT-4 without API keys.

❗ You must understand the following:
g4f is not an official OpenAI library and scrapes or reverse-engineers public endpoints.

This may break frequently, stop working without notice, or violate service terms.

Avoid using it for production, critical projects, or anything involving sensitive user data.

If unsure, replace it with OpenAI's official API and insert your key like so:

python
Copy
Edit
import openai

openai.api_key = "YOUR_API_KEY"
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[{"role": "user", "content": prompt}]
)
🔧 Configuration
Update your MySQL credentials in quiz_generator.py.

Ensure student_data.json is writable and in the root directory.

Add initial quiz data in your MySQL database under quiz_db.

📁 File Structure
bash
Copy
Edit
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
🧠 Topics Covered
Subjects: Data Science, Computer Science, Mathematics
Topics include:

MySQL, DSA, Pandas, NumPy, Power BI, EDA

Algorithms, OS, Networking

Calculus, Linear Algebra, Probability

🤝 Contributing
PRs are welcome! Open an issue for new features, bug fixes, or enhancements.

📜 License
This project is for educational and personal use only.
Please do not use g4f or this system in production without understanding its legal and ethical implications.

📬 Contact
Questions or suggestions? DM me or raise a GitHub issue.

python
Copy
Edit

---

Let me know if you'd like a production-safe version that replaces `g4f` with OpenAI's official API calls.





You said:
like keep it just in a warning section


ChatGPT said:
Got it. Here's a concise README.md with just the essential sections and a focused ⚠️ WARNING section for g4f—keeping it simple, clean, and practical for GitHub:

markdown
Copy
Edit
# 🤖 AI Tutor – Personalized Learning System

A Streamlit-based AI tutor that helps students personalize their learning with AI-powered quizzes, mastery prediction, convex optimization, and topic recommendations.

---

## 🚀 Features

- Ask questions to an AI tutor (GPT-powered)
- Take quizzes based on subject and level
- Predict your topic mastery using NLP
- Optimize your study time using convex optimization
- Get smart topic recommendations based on performance

---

## 📦 How to Run

```bash
pip install -r requirements.txt
streamlit run main.py
⚠️ WARNING: g4f Dependency
This project uses the g4f library to access GPT models without an API key. Please read this carefully:

g4f is unofficial, experimental, and not supported by OpenAI.

It may break suddenly, be inconsistent, or violate terms of service.

Do not use in production or with real user data.

Replace it with OpenAI’s official API in quiz_generator.py if needed:

python
Copy
Edit
import openai

openai.api_key = "YOUR_API_KEY"
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[{"role": "user", "content": prompt}]
)
Use g4f at your own risk. You’ve been warned.

🧠 Topics Covered
Subjects: Data Science, Computer Science, Mathematics

Examples: MySQL, DSA, ML, Stats, Python, OS, Algorithms, Calculus, Linear Algebra

📁 Files
main.py – UI logic

quiz_generator.py – AI and quiz database

tutor_backend.py – progress tracking

convex_optimizer.py – study time optimization

mastery_predictor.py – NLP-based scoring

recommendation_ui.py – topic suggestions

🛠️ Setup Notes
Ensure you have a MySQL database configured for quizzes.

student_data.json is used for saving student progress.

yaml
Copy
Edit
