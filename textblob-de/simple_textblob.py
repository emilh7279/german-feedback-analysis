from textblob_de import TextBlobDE as TextBlob
#import nltk
#nltk.download('punkt')

def satz_bewertung(satz):
    """
    Bewertet die Stimmung eines deutschen Satzes (positiv, negativ oder neutral).
    """
    # Erstellen eines TextBlob-Objekts
    blob = TextBlob(satz)

    # Polarität des Satzes analysieren
    polarität = blob.sentiment.polarity

    # Stimmungsbewertung basierend auf Polarität
    if polarität > 0:
        return f"Der Satz ist positiv. Polarität: {polarität}"
    elif polarität < 0:
        return f"Der Satz ist negativ. Polarität: {polarität}"
    else:
        return f"Der Satz ist neutral. Polarität: {polarität}"


# Testen mit einigen Beispielsätzen
sätze = [
    "Ich liebe dieses Wetter.",
    "Das Essen schmeckt schrecklich!",
    "Heute ist ein ganz normaler Tag.",
    "Die Frau arbeitet langsam!",
    "Die Frau kocht fantastisch"
]

for satz in sätze:
    print(satz_bewertung(satz))
