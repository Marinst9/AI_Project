# AI Emotion Detection Dashboard 🎭

A web application that combines AI, SQL database and real-time data visualization.

## What does it do?
Type any sentence and the AI model (DistilRoBERTa) will detect exactly how you feel — happy, angry, sad, surprised and more.

## Key Features
- **AI Analysis:** Uses Hugging Face Transformers to recognize 6 different emotions
- **Database:** SQLite stores all previous analyses so nothing is lost
- **Dashboard:** Streamlit web app displays results with real-time charts

## Tech Stack
Python • Hugging Face • Streamlit • SQLite • Pandas • Matplotlib • PyTorch

## How to run locally

1. Install dependencies:
pip install transformers streamlit pandas matplotlib torch

2. Start the app:
python -m streamlit run dashboard.py



## About
Built to learn how data flows from raw text → AI model → SQL database → visual dashboard.
