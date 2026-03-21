# 📊 Cryptocurrency Volatility Prediction

## 🚀 Overview

This project focuses on predicting cryptocurrency volatility using machine learning techniques. The goal is to analyze historical market data and build a model that can estimate future volatility patterns, helping in better risk assessment and decision-making.

---

## 🎯 Problem Statement

Cryptocurrency markets are highly volatile, making it difficult for investors and analysts to manage risk.
This project aims to:

* Analyze historical crypto price data
* Identify volatility patterns
* Build a predictive model for volatility estimation

---

## 📂 Dataset

* Historical OHLCV (Open, High, Low, Close, Volume) data
* Data spans multiple cryptocurrencies over several years
* Includes 72,000+ rows of processed data

---

## 🛠️ Approach

### 1. Data Cleaning & Preprocessing

* Handled missing and inconsistent values
* Removed infinite values
* Standardized data for analysis

### 2. Exploratory Data Analysis (EDA)

* Analyzed volatility trends across different cryptocurrencies
* Compared large-cap vs small-cap behavior
* Identified patterns in price fluctuations

### 3. Feature Engineering

Engineered meaningful financial indicators:

* Bollinger Bands
* Average True Range (ATR)
* Rolling Volatility
* Moving Averages
* Momentum Indicators

---

## 🤖 Model Development

* Model Used: **Random Forest Regressor**
* Reason: Handles non-linear relationships and complex feature interactions effectively

---

## 📈 Results

* Evaluated model using RMSE and R² score
* Model shows strong predictive capability on processed dataset
* Performance validated to reduce overfitting and improve generalization

---

## 🔍 Key Insights

* Smaller-cap cryptocurrencies tend to show higher volatility
* Market fluctuations are strongly influenced by momentum indicators
* Feature engineering significantly improves prediction performance

---

## 💾 Model Saving

* Saved trained model and scaler using **Joblib**
* Enables reuse and deployment

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/kirtivish974/Cryptocurrency-Volatility-Prediction-Project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the notebook:

* Open Jupyter Notebook
* Execute all cells

---

## 🧰 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn

---

## 📌 Future Improvements

* Hyperparameter tuning for better performance
* Try advanced models (XGBoost, LSTM)
* Deploy as a web application

---

## 🙋‍♀️ Author

**Kirti Vishwakarma**

* GitHub: https://github.com/kirtivish974
