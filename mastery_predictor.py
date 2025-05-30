import tensorflow_hub as hub
import numpy as np
import streamlit as st

@st.cache_resource
def load_use_model():
    return hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

model = load_use_model()

def get_mastery_score(statement):
    embedding = model([statement]).numpy()[0]
    score = np.linalg.norm(embedding)
    return round(min(score, 10), 2)

def get_mastery_for_topics(topics, feedbacks):
    return {topic: get_mastery_score(fb) for topic, fb in zip(topics, feedbacks)}
