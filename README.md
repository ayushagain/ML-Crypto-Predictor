# CryptoPredictor

## Predicting Cryptocurrency Prices with ML

CryptoPredictor is a machine learning-powered app that forecasts cryptocurrency prices. Built with Python and Streamlit, it leverages historical data to predict trends for popular cryptocurrencies, providing users with data-driven insights.

---

## 🏗️ Project Structure

```
CryptoPredictor  
├── assets/         
│   ├── dataCleaning/
│   │   ├── CoinGeckoToCsv.ipynb   
│   │   └── cryptoTickers.csv
│   └── gifs/               
│       └── crypto.gif
├── streamlit_app/
│   ├── modules/
│   │   └── helper.py
│   ├── pages/               
│   │   └── 01_₿__CryptoPredictor.py
│   └── 00_🛈_Info.py        
├── LICENSE                 
├── README.md               
└── requirements.txt        
```

---

## 🛠️ Built With

- **Streamlit** - Interactive UI for easy usability.
- **Yahoo Finance API (YFinance)** - Fetches up-to-date cryptocurrency data.
- **CoinGecko API** - Retrieves top 2,500 cryptocurrencies by market capitalization.
- **LSTM (Long Short-Term Memory)** - Optimized for time-series predictions.
- **Plotly** - Creates interactive financial charts.
- **Pandas** - Handles cryptocurrency dataset processing.

---

## 🚀 How It Works

1. Select a cryptocurrency (e.g., BTC, ETH).
2. Retrieve historical price data via Yahoo Finance API.
3. Train an LSTM model on the past 60 days of data.
4. Generate predictions for 1–90 days.
5. View results with interactive charts and tables.

---

## ✨ Features

- 📊 **Real-time cryptocurrency data** - Always up-to-date.
- 📈 **Interactive charts** - Visualize trends and predictions.
- ⏳ **Custom prediction ranges** - Forecast for 1 to 90 days.
- 📥 **Downloadable CSV** - Export results for further analysis.
- 🖥️ **User-friendly interface** - Accessible to all experience levels.

---

## 🔧 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/josericodata/CryptoPredictor.git
```

### 2️⃣ Navigate to Project Directory
```bash
cd CryptoPredictor
```

### 3️⃣ Create and Activate Virtual Environment
```bash
python3 -m venv venvCrypto
source venvCrypto/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application
```bash
cd streamlit_app
streamlit run 00_🛈_Info.py
```
The app will be available at: **http://localhost:8501**

---

## 🎬 Demo

![Crypto Predictor](assets/gifs/crypto.gif)

▶️ **Watch the YouTube Tutorial**
[Crypto Predictor App in 3 Minutes with Streamlit](#)

---

## 🔮 Future Enhancements

- 📈 **Advanced ML models (e.g., Prophet) for improved accuracy.**
- 🌍 **Support for more cryptocurrencies.**
- 📊 **Volatility analysis to assess risks.**
- 🔐 **User accounts for personalized predictions.**

---

## 📋 Important Notes

- **CoinGecko API Error 429:** If you make too many requests, the API may temporarily block access. Restart the app after a few minutes.
- **Using CryptoPredictor:**
  - Choose a cryptocurrency.
  - Select the prediction range.
  - Adjust epochs (higher values may improve accuracy but take longer to train).
  - Click **Run Prediction** to see results.

---

## 🤝 Contributions & Support

- Found a bug? Open a pull request on GitHub.
- For inquiries, email: **maninastre@gmail.com**

---

## ⚠️ Disclaimer

CryptoPredictor is a demonstration of machine learning in financial forecasting. It is not financial advice. Predictions are for educational purposes only and should not be relied upon for investment decisions.

Happy Learning - Ayush
