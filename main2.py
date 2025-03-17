from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import re

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("financial_sentiment_lstm.h5")

# Load the tokenizer
with open("tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)

MAX_SEQUENCE_LENGTH = 300

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def fetch_news_content(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all('p')
            return ' '.join([p.get_text(separator=' ') for p in paragraphs]).strip()
        return ""
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return ""

def preprocess_text(text):
    text = clean_text(text)
    if not text:
        return np.zeros((1, MAX_SEQUENCE_LENGTH))
    sequences = tokenizer.texts_to_sequences([text])
    if not sequences or sequences == [[]]:
        return np.zeros((1, MAX_SEQUENCE_LENGTH))
    return pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding="post", truncating="post")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    news_url = data.get("news_url")
    
    if not news_url:
        return jsonify({"error": "No URL provided"}), 400

    news_content = fetch_news_content(news_url)
    
    if not news_content:
        return jsonify({"error": "Could not fetch news content or content is empty."}), 400

    processed_text = preprocess_text(news_content)
    prediction = model.predict(processed_text)[0][0]
    sentiment = "Positive" if prediction > 0.5 else "Negative"
    
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
