import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
import re
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Load dataset
file_path = "FinancialMarketNews.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Merge all news columns into a single text column
news_columns = [col for col in df.columns if "News" in col]
df[news_columns] = df[news_columns].fillna("")
df["Combined_News"] = df[news_columns].apply(lambda x: " ".join(x), axis=1)
df = df[["Combined_News", "Label"]]

# Text Cleaning Function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Clean the text data
df["Combined_News"] = df["Combined_News"].apply(clean_text)

# Tokenization
MAX_VOCAB_SIZE = 10000
MAX_SEQUENCE_LENGTH = 300
tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE, oov_token="<OOV>")
tokenizer.fit_on_texts(df["Combined_News"])

# Save tokenizer
with open("tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Tokenizer has been saved successfully.")

# Convert text to sequences
sequences = tokenizer.texts_to_sequences(df["Combined_News"])
padded_sequences = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding="post", truncating="post")
labels = np.array(df["Label"])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42, stratify=labels)

# Build LSTM model
model = Sequential([
    Embedding(input_dim=MAX_VOCAB_SIZE, output_dim=128, input_length=MAX_SEQUENCE_LENGTH),
    LSTM(128, return_sequences=True),
    Dropout(0.3),
    LSTM(64),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save model
model.save("financial_sentiment_lstm.h5")
print("Model training complete and saved as 'financial_sentiment_lstm.h5'.")
