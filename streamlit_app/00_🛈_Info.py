import streamlit as st
from datetime import datetime

# Set up the Streamlit page configuration
st.set_page_config(page_title="CryptoForecaster", page_icon="🚀")

# Generate the current timestamp dynamically
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main content of the app
st.markdown(
    """# 🚀 **CryptoForecaster**
### **AI-Powered Cryptocurrency Price Predictions**

**CryptoForecaster** is a cutting-edge machine learning application designed to predict cryptocurrency prices. Built by **Ayush (ayushagain)**, this app leverages historical data and advanced algorithms to forecast trends for popular cryptocurrencies, empowering users with actionable insights.

## 🛠️ **Tech Stack**

CryptoForecaster is built using the following tools and frameworks:

- **Streamlit** - For creating an intuitive and interactive web interface.
- **Yahoo Finance API (YFinance)** - To fetch real-time cryptocurrency data.
- **CoinGecko API** - To dynamically retrieve the top 2,500 cryptocurrencies by market cap from a pool of over 17,000 tokens. For an updated list of tickers, check out the Jupyter Notebook: [CoinGeckoToCsv.ipynb](https://github.com/ayushagain/CryptoForecaster/blob/main/assets/dataCleaning/CoinGeckoToCsv.ipynb).
- **LSTM (Long Short-Term Memory)** - A neural network model optimized for time-series forecasting.
- **Plotly** - For generating dynamic and interactive financial charts.
- **Pandas** - For data manipulation and processing.

## 🧑‍💻 **How It Works**

1. **Select a Cryptocurrency**: Choose from popular options like BTC, ETH, or others.
2. **Fetch Historical Data**: The app retrieves historical price data using Yahoo Finance.
3. **Train the Model**: The LSTM model is trained on the past 60 days of data.
4. **Generate Predictions**: Forecast prices for the next 1–90 days.
5. **Visualize Results**: Explore predictions through interactive charts and tables.

## ✨ **Key Features**

- **Real-Time Data**: Access up-to-date cryptocurrency prices.
- **Interactive Visualizations**: View trends and predictions with dynamic charts.
- **Customizable Predictions**: Forecast prices for 1 to 90 days.
- **Downloadable Results**: Save predictions as CSV files for further analysis.
- **User-Friendly Design**: Simple and intuitive for both beginners and experts.

## 🚀 **Getting Started**

### **Local Setup**

1. Clone the repository:
```bash
git clone https://github.com/ayushagain/CryptoForecaster.git
