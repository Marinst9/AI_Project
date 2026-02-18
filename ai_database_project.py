import sqlite3
from transformers import pipeline


conn = sqlite3.connect('emocii.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS analizi 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, tekst TEXT, emocija TEXT, score REAL)''')
conn.commit()


print("⏳ Го вчитувам моделот за емоции (овој е подетален)...")
emotion_classifier = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

test_sentences = [
    "I am so proud of my AI project!",
    "I feel terrified about the exam tomorrow.",
    "Stop doing that, it's making me so angry!",
    "I'm surprised how easy this became with your help.",
    "It's a lonely night and I miss my friends."
]

print("🚀 Почнувам со анализа и зачувување во SQL база...")

for sentence in test_sentences:
    result = emotion_classifier(sentence)[0]
    emocija = result['label']
    tochnost = result['score']
    
    cursor.execute("INSERT INTO analizi (tekst, emocija, score) VALUES (?, ?, ?)", 
                   (sentence, emocija, tochnost))
    
    print(f"✅ Анализирано: {emocija} | Текст: {sentence[:30]}...")

conn.commit()
conn.close()
print("\n💾 Сите податоци се безбедно зачувани во 'emocii.db'!")