
# Cryptocurrency Volatility Prediction Project

A machine learning project that predicts cryptocurrency price volatility using historical market data and feature engineering techniques.

## 📋 Project Overview

This project aims to build a predictive model that forecasts cryptocurrency market volatility. The model analyzes historical market data and engineered features to predict future price movements, helping traders and investors make informed decisions.

**Target**: Predict volatility levels for cryptocurrencies  
**Approach**: Machine Learning (Supervised Learning)  
**Deployment**: Streamlit Web Application

---

## 🎯 How the Project Works

### 1. **Data Ingestion & Preprocessing**
   - Collect historical cryptocurrency market data (price, volume, returns)
   - Load and clean the data from `data/processed_dataset.csv`
   - Handle missing values and data inconsistencies
   - Normalize and scale features for model training

### 2. **Feature Engineering**
   - Create meaningful features from raw market data:
     - Technical indicators (moving averages, RSI, MACD, etc.)
     - Price-based features (returns, price changes, momentum)
     - Volume-based features (trading volume, volume moving averages)
     - Volatility-based features (historical volatility, standard deviation)
   - Select most relevant features for the model

### 3. **Model Training**
   - Train a machine learning model on historical data
   - Use the processed dataset to fit the model
   - Apply various algorithms and select the best performing one
   - Save the trained model as `models/volatility_model.pkl`

### 4. **Model Evaluation**
   - Evaluate model performance on test data:
     - **RMSE**: 0.0573 (Root Mean Squared Error)
     - **MAE**: 0.0433 (Mean Absolute Error)
     - **R² Score**: -0.493 (Coefficient of Determination)

### 5. **Web Application**
   - Deploy the model using Streamlit
   - Users can upload CSV files with feature data
   - Get real-time volatility predictions
   - Interactive interface for easy access

---

## 📁 Project Structure

```
Crypto_Volatility_Prediction_Project/
│
├── README.md                          # Project documentation
│
├── data/
│   └── processed_dataset.csv          # Cleaned and processed dataset
│
├── docs/
│   ├── HLD.md                         # High-Level Design document
│   └── LLD.md                         # Low-Level Design document
│
├── models/
│   └── volatility_model.pkl           # Trained machine learning model
│
├── plots/                             # Visualization files (graphs, charts)
│
├── reports/                           # Analysis and results reports
│
└── streamlit_app/
    └── app.py                         # Streamlit web application
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Required Python packages: pandas, scikit-learn, streamlit, joblib

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Crypto_Volatility_Prediction_Project
   ```

2. **Install dependencies**
   ```bash
   pip install pandas scikit-learn streamlit joblib numpy matplotlib
   ```

### Running the Application

1. **Navigate to the streamlit app directory**
   ```bash
   cd streamlit_app
   ```

2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

3. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`
   - Upload a CSV file with the required feature columns
   - View the predicted volatility values

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| RMSE | 0.0573 |
| MAE | 0.0433 |
| R² Score | -0.4930 |

**Note**: The current R² score indicates the model has room for improvement. Consider:
- Adding more relevant features
- Trying different algorithms
- Tuning hyperparameters
- Collecting more training data

---

## 📝 Data Format

The input CSV file should contain the following feature columns:
- Market price data
- Trading volume
- Technical indicators
- Historical volatility measures

Refer to `data/processed_dataset.csv` for the expected data format.

---

## 🔄 Workflow

```
Data Ingestion → Data Cleaning → Feature Engineering → Model Training → 
Evaluation → Deployment (Streamlit App)
```

---

## 💡 Use Cases

- **Traders**: Predicting market volatility for strategy planning
- **Risk Analysts**: Assessing cryptocurrency market risk
- **Investors**: Making informed investment decisions
- **Researchers**: Studying market behavior patterns

---

## 🛠️ Technologies Used

- **Python**: Main programming language
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **Streamlit**: Web application framework
- **Joblib**: Model serialization

---

## 📚 Documentation

- **HLD.md**: High-level architecture and workflow
- **LLD.md**: Detailed module breakdown and implementation
- **processed_dataset.csv**: Data dictionary and feature descriptions

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

---

**Last Updated**: February 2026
