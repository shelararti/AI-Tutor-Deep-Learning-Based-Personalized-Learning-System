import streamlit as st
import g4f
import mysql.connector

# === Answer a Student's Question ===
def answer_student_question(question, level="beginner"):
    prompt = f"Answer this question in a helpful, simple way for a {level}-level student: {question}"
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",       # e.g., "localhost"
        user="root",   # e.g., "root"
        password="2H&BIk!yG9AjZ7HJ",
        database="quiz_db"
    )

# Function to fetch quizzes based on selected topic and level
def get_quiz_from_db(topic_name, level_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT q.question, q.option_a, q.option_b, q.option_c, q.option_d, q.correct_option, q.explanation
        FROM quizzes q
        JOIN topics t ON q.topic_id = t.id
        JOIN levels l ON q.level_id = l.id
        WHERE t.name = %s AND l.name = %s
    """
    
    cursor.execute(query, (topic_name, level_name))
    quizzes = cursor.fetchall()
    conn.close()
    return quizzes

# Function to generate quiz for the user
def generate_quiz(topic_name, level_name):
    quizzes = get_quiz_from_db(topic_name, level_name)
    
    if not quizzes:
        st.warning("No quizzes available for this topic and level.")
        return []

    quiz_data = []
    for quiz in quizzes:
        quiz_data.append({
            "question": quiz["question"],
            "options": [
                {"text": quiz["option_a"], "is_correct": quiz["correct_option"] == 'A'},
                {"text": quiz["option_b"], "is_correct": quiz["correct_option"] == 'B'},
                {"text": quiz["option_c"], "is_correct": quiz["correct_option"] == 'C'},
                {"text": quiz["option_d"], "is_correct": quiz["correct_option"] == 'D'}
            ],
            "explanation": quiz["explanation"]
        })
    
    return quiz_data
