# Financial News Sentiment Analysis

This project is a **Financial News Sentiment Analysis** tool built using **Flask** (Python) for the backend and **HTML, CSS, and JavaScript** for the frontend. It allows users to input a URL of financial news, processes the text, and predicts whether the sentiment is **Positive** or **Negative** using a trained **LSTM model**.

---

## 🚀 Features
- **Web Scraping**: Extracts news content from the given URL.
- **Text Preprocessing**: Cleans and tokenizes the text.
- **Sentiment Prediction**: Utilizes an LSTM model for predicting sentiment.
- **Interactive Frontend**: User-friendly interface to input URLs and view results.

---

## 🏗️ Project Structure
```
Financial_news/
├── brainrot.py
├── main2.py                  # Flask application
├── FinancialMarketNews.csv    # Dataset (if applicable)
├── financial_sentiment_lstm.h5 # Trained LSTM model
├── tokenizer.pickle           # Tokenizer for text preprocessing
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # Main HTML page
├── static/
│   ├── css/
│   │   └── styles.css         # CSS styles
│   └── js/
│       └── script.js          # JavaScript logic
```

---

## ⚙️ Installation

1. **Clone the Repository:**
```bash
git clone <repository-url>
cd Financial_news
```

2. **Create a Virtual Environment (Optional):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Application:**
```bash
python main2.py
```

5. **Visit the Application:**
- Open your browser and navigate to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📄 API Endpoint

### `POST /predict`
- **Request Body (JSON):**
```json
{
  "news_url": "<URL of the financial news article>"
}
```
- **Response:**
```json
{
  "sentiment": "Positive" | "Negative"
}
```
- **Error Responses:**
```json
{
  "error": "Error message"
}
```

---

## 🖥️ Frontend Instructions
- Navigate to the home page.
- Paste the financial news article URL in the input field.
- Click **"Analyze Sentiment"** to view the sentiment result.

---

## 🛠️ Technologies Used
- **Backend:** Flask, TensorFlow, BeautifulSoup, Requests
- **Frontend:** HTML, CSS, JavaScript
- **Model:** LSTM (Long Short-Term Memory Neural Network)

---

## 🔄 Updating the Model
- Replace `financial_sentiment_lstm.h5` with the new trained model.
- Ensure the tokenizer (`tokenizer.pickle`) is updated if necessary.

---

## 🐛 Troubleshooting
- **Flask not running?**
  - Ensure you have activated your virtual environment.
  - Confirm Flask is installed in your environment.
- **Model errors?**
  - Verify the model and tokenizer files are correctly placed.
- **CORS Issues?**
  - If deploying to production, configure CORS in Flask.

---

## 📃 License
This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📞 Contact
- **Kush Pandya**
- [LinkedIn](#) | [GitHub](#)

---

> **Note:** Ensure that the URLs used for sentiment analysis are valid and accessible.
