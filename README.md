# 📊 German Sentiment Analysis for Service Desk Feedback with `TextBlob-de`, Hugging Face's BERT, and Custom Self-Trained Models

Welcome to the **German Sentiment Analysis** project, where we utilize **`TextBlob-de`**, **Hugging Face's BERT**, and **Custom Self-Trained Models** for analyzing customer feedback from a service desk. The goal is to detect and classify sentiments (positive, negative, neutral) in German feedback to improve service quality and customer experience.

----------

## 🎯 Project Background

Customer feedback from a service desk is invaluable for improving services. Whether it's praise for excellent support or dissatisfaction with unresolved issues, understanding customer sentiment allows for more informed decisions. This project focuses on analyzing German-language feedback from service desk interactions using **rule-based**, **pre-trained**, and **custom-trained deep learning models**.

By incorporating **Captain Self-Trained Models**, we add a flexible option for those looking to fine-tune sentiment analysis models specifically for their datasets, improving accuracy for niche domains or company-specific feedback.

----------

## 🚀 Features

-   **TextBlob-de**: A rule-based sentiment analysis tool for the German language.
-   **BERT** from Hugging Face: A pre-trained transformer model fine-tuned for sentiment analysis.
-   **Custom Self-Trained Models**: Models trained on company-specific service desk feedback for better domain adaptation..

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
