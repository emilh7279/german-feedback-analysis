# 📊 German Sentiment Analysis for Service Desk Feedback with `TextBlob-de`, Hugging Face's BERT, and Custom Self-Trained Models

Welcome to the **German Sentiment Analysis** project, where we utilize **`TextBlob-de`**, **Hugging Face's BERT**, and **Custom Self-Trained Models** for analyzing customer feedback from a service desk. The goal is to detect and classify sentiments (positive, negative, neutral) in feedback and use the results to generate Key Performance Indicators (KPIs) for tracking service desk performance and customer satisfaction.


----------

## 🎯 Project Background

Customer feedback from a service desk is invaluable for improving services. Whether it's praise for excellent support or dissatisfaction with unresolved issues, understanding customer sentiment allows for more informed decisions. This project focuses on analyzing German-language feedback from service desk interactions using **rule-based**, **pre-trained**, and **custom-trained deep learning models**.

The main goal of this project is to perform sentiment analysis on German-language customer feedback and create KPIs to measure:

-   The ratio of positive to negative feedback over time.
-   The percentage of neutral feedback, indicating customer indifference or satisfaction.
-   Sentiment trends that can help monitor service desk agent performance and customer satisfaction across different departments or time periods.

These KPIs will enable businesses to track the effectiveness of their customer support services, identify pain points, and optimize resource allocation.


----------

## 🚀 Features

-   **TextBlob-de**: A rule-based sentiment analysis tool for the German language.
-   **BERT** from Hugging Face: A pre-trained transformer model fine-tuned for sentiment analysis.
-   **Custom Self-Trained Models**: Models trained on company-specific service desk feedback for better domain adaptation.

----------

## 📚 Table of Contents

1.  [Installation](#installation)
2.  [Usage](#usage)
    -   [TextBlob-de Sentiment Analysis](#textblob-de-sentiment-analysis)
    -   [BERT Sentiment Analysis](#bert-sentiment-analysis)
    -   [Captain Self-Trained Model Analysis](#captain-self-trained-model-analysis)
3.  [Training Custom Models](#training-custom-models)
4.  [Model Performance](#model-performance)
5.  [Contributing](#contributing)
6.  [License](#license)

----------

## 🛠 Installation

### 1. Clone the repository:

    git clone https://github.com/emilh7279/german-feedback-analysis.git
cd german-sentiment-analysis

### 2. Create a virtual environment:

	  python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate


### 3. Install the dependencies:

    pip install -r requirements.txt` 

The following packages will be installed:

-   `textblob-de`
-   `transformers`
-   `torch`
-   `pandas`
-   `scikit-learn`

----------

## 💡 Usage

This repository provides three approaches to performing sentiment analysis on service desk feedback data: **TextBlob-de**, **BERT**, and **Finetuned BERT Models**. The idea is to use the results of the sentiment analysis to generate KPIs to track customer satisfaction.

### TextBlob-de Sentiment Analysis

`TextBlob-de` is a rule-based model that assigns polarity values to words and computes the overall sentiment of the text.

#### Example Usage: Feedback from a service desk

    from textblob_de import TextBlobDE
    
    feedback = "Der Service war schlecht, ich habe nie eine Antwort erhalten."
    
    blob = TextBlobDE(feedback)
    print("Sentiment Polarity:", blob.sentiment.polarity)` 

**Output:**
`Sentiment Polarity: -0.6`

### Folder textblob-de
The folder textblob-de contains two python files which shows the usage  of a sentiment analysis.

#### File simple_textblob.py
 ##### Function: `satz_bewertung(satz)`

This function evaluates the sentiment of a given German sentence and returns an assessment as **positive**, **negative**, or **neutral**. The sentiment is determined based on the **polarity** of the sentence, which is calculated through sentiment analysis.

##### Parameters:

-   `satz`: A string representing the German sentence to be analyzed.

#### How it works:

1.  **Create a TextBlob object**: First, a `TextBlob` object is created from the input sentence. This object allows the use of sentiment analysis methods.
    
2.  **Analyze polarity**: The function analyzes the polarity of the sentence using the method `blob.sentiment.polarity`. The polarity is a value ranging from -1 to 1:
    
    -   Values greater than 0 indicate that the sentence is positive.
    -   Values less than 0 indicate that the sentence is negative.
    -   A value of exactly 0 indicates that the sentence is neutral.
3.  **Sentiment evaluation**:
    
    -   If the polarity is positive (i.e., greater than 0), the function returns that the sentence is positive, along with the exact polarity value.
    -   If the polarity is negative (i.e., less than 0), the sentence is classified as negative.
    -   If the polarity is exactly 0, the sentence is classified as neutral.

#### Return:

-   A string that describes the sentiment of the sentence ("positive", "negative", "neutral") and includes the calculated polarity value.

#### Sample Input:

 1. Der Service war hervorragend und mein Anliegen wurde sofort geklärt.
 2. Der Prozess war etwas langwierig, aber das Endergebnis war in Ordnung.  
 3. Der Mitarbeiter war sehr unhöflich und mein Problem wurde nicht 	   behoben.
 4. Schlechter Kundenservice, niemand hat auf meine Anfragen geantwortet.
 5. Der Service hat zu lange gebraucht und mein Problem nicht gelöst.
 6. Ich bin wirklich beeindruckt, wie schnell mein Problem gelöst wurde.
 7. Fantastischer Service! Mein Problem wurde sofort gelöst.
 8. Es hat viel zu lange gedauert und niemand konnte mir helfen.
 9. Es war okay, nicht das Beste, aber das Problem wurde gelöst.
 10. Das Support-Team schien verwirrt und hat nicht wirklich geholfen.

#### Sample Output:

 1. Der Satz ist positiv. Polarität: 1.0
 2. Der Satz ist neutral. Polarität: 0.0
 3. Der Satz ist negativ. Polarität: -1.0
 4. Der Satz ist negativ. Polarität: -1.0
 5. Der Satz ist neutral. Polarität: 0.0
 6. Der Satz ist positiv. Polarität: 0.85
 7. Der Satz ist positiv. Polarität: 0.5
 8. Der Satz ist positiv. Polarität: 0.35
 9. Der Satz ist neutral. Polarität: 0.0
 10. Der Satz ist negativ. Polarität: -0.75

--------

#### File sentiment_feedback_textblob.py
This script includes, in addition to the satz_bewertung(satz) function,
functions for reading a larger dataset in CSV format and saving the determined sentiments in a CSV file.

##### Function: lade_saetze(dateiname)
This function loads sentences from a CSV file that contains feedback data. The filename is passed as a parameter,
and the function extracts the text column from the CSV file and returns it as a list of sentences.

> [!IMPORTANT]  
> The CSV file must be placed in the input_data folder.

##### Parameters:
dateiname: A string that specifies the name of the CSV file containing the feedback data.

##### Function: speichere_ergebnisse(ergebnisse)
This function saves the results of an analysis into a CSV file.
The results are stored in a structured way, making them easy to view or process later.

> [!NOTE]
> The result CSV file is located in textblob-de/results.

--------
#### Conclusion TextBlob-DE
As you can see TextBlob is a fast and easy-to-use method for performing sentiment analysis on sentences.
With textblob-de, the framework also provides a direct way to interpret German sentences.