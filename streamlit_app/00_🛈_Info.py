import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Crypto Forecast", page_icon="💰")

# Generate the current timestamp dynamically
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(
    """# 💰 **CryptoForecast**
### **AI-Powered Cryptocurrency Predictions**

**CryptoForecast is an advanced ML-based application designed to predict cryptocurrency trends. Built using Python and Streamlit, it leverages historical market data to provide insightful forecasts, helping users make data-informed decisions.**

## 🛠️ **Core Technologies**

CryptoForecast is powered by:

- **Streamlit** - For an interactive and user-friendly web interface.
- **Yahoo Finance API** - To fetch real-time cryptocurrency market data.
- **CoinGecko API** - Provides access to top cryptocurrencies based on market capitalization.
- **LSTM (Long Short-Term Memory)** - A deep learning model optimized for time-series forecasting.
- **Plotly** - For generating interactive and dynamic financial visualizations.
- **Pandas** - For effective data manipulation and analysis.

## 🧑‍💻 **How It Works**

1. Choose a cryptocurrency (e.g., BTC, ETH).
2. Fetch historical market data from Yahoo Finance.
3. Train the LSTM model on the last 60 days of data.
4. Generate price forecasts for 1–90 days.
5. Visualize predictions through interactive charts.

## ✨ **Key Features**

- **Live market data** - Get real-time updates on cryptocurrency prices.
- **Custom prediction range** - Forecast prices for up to 90 days.
- **Interactive graphs** - Analyze past trends and future predictions visually.
- **Downloadable reports** - Save predictions for future reference.
- **Beginner-friendly UI** - Simple and easy-to-use interface for all users.

## 🚀 **Getting Started**

### **Local Installation**

1. Clone the repository:
```bash
git clone https://github.com/ayushagain/CryptoForecast.git
```

2. Navigate to the project folder:
```bash
cd CryptoForecast
```

3. Create and activate a virtual environment:
```bash
python3 -m venv venvCrypto
source venvCrypto/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Navigate to the app folder:
```bash
cd streamlit_app
```

6. Launch the app:
```bash
streamlit run main.py
```

The application will be accessible at ```http://localhost:8501```.

## 🌟 Future Enhancements

Upcoming features include:

- **Integration of advanced ML models** (e.g., Prophet) for enhanced accuracy.
- **Expanded cryptocurrency support** to cover more digital assets.
- **Risk assessment tools** for better decision-making.
- **User accounts** to save preferences and prediction history.

## 🔧 System Requirements

CryptoForecast has been tested on:

- **OS**: Ubuntu 22.04.5 LTS
- **Python Version**: 3.10.12

Ensure your system meets these requirements for the best experience.

## 📋 Important Notes

- **API Request Limits**: Excessive requests to CoinGecko may lead to temporary restrictions. If you encounter issues, wait a few minutes before retrying.
- **How to Use**:
    1. Select a cryptocurrency from the dropdown.
    2. Set the prediction range using the slider.
    3. Adjust **Epochs** to control training time and model accuracy.
    4. Click **Run Prediction** to generate forecasts.

## ⚠️ Disclaimer

This app is developed for educational and portfolio-building purposes. It does not provide financial advice. All predictions are for informational use only and should not be used for investment decisions.
"""
)

# Display the timestamp in a Streamlit app
st.write("### 🔄 Last Updated")
st.write(f"The app was last updated on: **{current_timestamp}**")
