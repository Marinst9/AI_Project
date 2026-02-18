import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

emotion_classifier = load_model()

st.set_page_config(page_title="Marina's AI Dashboard", layout="wide")
st.title("🎭 Interactive Emotion Analytics")


st.subheader("📝 Внеси своја реченица за анализа")
user_input = st.text_input("Напиши нешто на англиски:")

if st.button('Анализирај и зачувај'):
    if user_input:
        result = emotion_classifier(user_input)[0]
        emocija = result['label']
        score = result['score']
        
      
        conn = sqlite3.connect('emocii.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO analizi (tekst, emocija, score) VALUES (?, ?, ?)", 
                       (user_input, emocija, score))
        conn.commit()
        conn.close()
        
        st.success(f"Резултат: {emocija} (со {score:.2%} сигурност) е додаден во базата!")
    else:
        st.warning("Ве молам внесете текст.")


def get_data():
    conn = sqlite3.connect('emocii.db')
    df = pd.read_sql_query("SELECT * FROM analizi", conn)
    conn.close()
    return df

data = get_data()

st.divider()
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Историја на анализи")
    st.dataframe(data.tail(10), use_container_width=True)

with col2:
    st.subheader("📊 Статистика")
    emotion_counts = data['emocija'].value_counts()
    fig, ax = plt.subplots()
    emotion_counts.plot(kind='bar', color='skyblue', ax=ax)
    st.pyplot(fig)