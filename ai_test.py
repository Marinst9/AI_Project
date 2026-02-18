from transformers import pipeline

print("⏳ Го вчитувам локалниот модел (чекај малку)...")

try:
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    test_text = "I am so confused and lost, but at the same time, I am excited to learn something new!"
    
    print(f"🔍 Анализирам текст: '{test_text}'")
    
    result = classifier(test_text)

    print("\n🤖 РЕЗУЛТАТ ОД ЛОКАЛНИОТ AI:")
    label = result[0]['label']
    score = result[0]['score']
    print(f"Чувство: {label} (со точност од {score:.2%})")

except Exception as e:
    print(f"\n❌ Грешка при вчитување: {e}")