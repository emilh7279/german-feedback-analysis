import os
import csv
import datetime as dt
from pathlib import Path
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Add to rquiremnts
# pip install urllib3==1.26.6

# 1. Lade das vortrainierte deutsche BERT-Modell und den Tokenizer
model_name = "oliverguhr/german-sentiment-bert"  # Ein feingetuntes Sentiment-Modell für deutsche Sprache
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# 2. Funktion zur Sentiment-Analyse
def analyse_sentiment(text):
    # Text tokenisieren
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Vorhersage mit dem Modell
    with torch.no_grad():
        outputs = model(**inputs)

    # Die Logits werden in Wahrscheinlichkeiten umgewandelt (softmax)
    probs = F.softmax(outputs.logits, dim=-1)

    # Die Klasse mit der höchsten Wahrscheinlichkeit bestimmen
    sentiment = torch.argmax(probs).item()
    sentiment_label = ["negative", "neutral", "positive"][sentiment]

    return sentiment_label, probs[0][sentiment].item()


# 3. Teste die Funktion mit einem deutschen Satz
text = "Der Mitarbeiter war sehr unhöflich und mein Problem wurde nicht behoben"
sentiment, confidence = analyse_sentiment(text)

print(f"Text: {text}")
print(f"Sentiment: {sentiment} (Confidence: {confidence:.4f})")
