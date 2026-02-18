from transformers import pipeline
import time

print("⏳ Се подготвувам за анализа...")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


raw_data = [
    "I love this new technology, it's going to change everything!",
    "This is a complete scam, do not invest your money.",
    "The market is a bit slow today, but I am hopeful.",
    "I don't know what to think, it's very confusing.",
    "Best experience ever, the community is so helpful!"
]

print(f"📦 Примени се {len(raw_data)} коментари. Почнувам со обработка...\n")

results = []

for i, comment in enumerate(raw_data, 1):
    print(f"Анализирам коментар бр. {i}...")
    
    analysis = classifier(comment)[0]
    
    entry = {
        "text": comment,
        "sentiment": analysis['label'],
        "confidence": round(analysis['score'] * 100, 2)
    }
    results.append(entry)
    time.sleep(0.5) 

print("\n--- ГЕНЕРИРАН ИЗВЕШТАЈ ---")
positives = len([r for r in results if r['sentiment'] == 'POSITIVE'])
negatives = len([r for r in results if r['sentiment'] == 'NEGATIVE'])

print(f"✅ Позитивни мислења: {positives}")
print(f"❌ Негативни мислења: {negatives}")
print("--------------------------")


for r in results:
    emoji = "😊" if r['sentiment'] == 'POSITIVE' else "😡"
    print(f"{emoji} [{r['sentiment']}] - {r['text']} ({r['confidence']}% сигурност)")

   
with open("izvestaj.txt", "w", encoding="utf-8") as f:
    f.write("ФИНАЛЕН ИЗВЕШТАЈ ОД AI АНАЛИЗАТА\n")
    f.write(f"Позитивни: {positives}, Негативни: {negatives}\n\n")
    for r in results:
        f.write(f"[{r['sentiment']}] {r['text']}\n")

print("\n📁 Извештајот е зачуван во 'izvestaj.txt'!")

import matplotlib.pyplot as plt


labels = ['Positive 😊', 'Negative 😡']
sizes = [positives, negatives]
colors = ['#66ff66', '#ff6666']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('AI Анализа на чувства - Резултати')

plt.savefig('grafikon_rezultati.png')
print("\n📊 Графиконот е генериран како 'grafikon_rezultati.png'!")

plt.show()