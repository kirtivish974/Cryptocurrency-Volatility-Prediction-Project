# Crypto Volatility Prediction (Machine Learning)

A machine learning project that analyzes cryptocurrency market data and predicts price volatility using regression models. The project explores relationships between market indicators and volatility to understand which factors drive unstable price behavior in crypto assets.

---

## Project Goal

Cryptocurrency markets are highly volatile, which creates both opportunity and risk. The goal of this project is to:

- Analyze historical crypto market data  
- Identify features that influence volatility  
- Build a machine learning model to predict volatility  
- Evaluate model performance using standard regression metrics  

This project demonstrates a **complete beginner-friendly ML workflow from raw data to model evaluation**.

---

## Project Pipeline

The project follows a typical data science workflow:

1. Data Collection and Loading  
2. Data Cleaning and Preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. Model Training  
6. Model Evaluation  
7. Model Saving for Future Use  

---

## Exploratory Data Analysis

Several patterns emerged during data exploration.

Key observations:

- Smaller cryptocurrencies tend to show **higher volatility**
- Trading volume alone does **not strongly explain volatility**
- Daily returns are **highly correlated with volatility**
- Some altcoins show extreme fluctuations compared to large-cap coins

### Feature Correlation

| Feature | Correlation with Volatility |
|--------|--------|
| Volume | -0.014 |
| Market Cap | -0.009 |
| Daily Return | 0.94 |

Daily returns turned out to be the **strongest predictive feature**.

---

## Models Used

Two regression models were tested:

### 1. Linear Regression
- Used as a baseline model
- Helps understand linear relationships between features

### 2. Random Forest Regressor
- Ensemble learning model
- Captures nonlinear relationships
- Performs better on complex datasets

Because this is time-based data, the dataset was split **chronologically instead of randomly** to prevent data leakage.

Train/Test split:

- **80% Training**
- **20% Testing**

---

## Model Performance

Final model used: **Random Forest Regressor**

| Metric | Score |
|------|------|
| RMSE | 0.035 |
| MAE | 0.015 |
| R² Score | 0.75 |

The model explains approximately **75% of the variance in cryptocurrency volatility**.

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Joblib  
- Jupyter Notebook  

---

## Project Structure


crypto-volatility-prediction
│
├── data
│ └── crypto_data.csv
│
├── notebooks
│ └── Crypto_volatility_prediction.ipynb
│
├── model
│ └── crypto_model.pkl
│
└── README.md


---

## Model Saving

The trained model is saved using Joblib.

python
import joblib
joblib.dump(model, "crypto_model.pkl")

This allows the model to be reused later for predictions or deployment.

---
## How to Run the Project

1. Clone the repository
git clone https://github.com/yourusername/crypto-volatility-prediction.git
2. Install dependencies
pip install pandas numpy matplotlib scikit-learn joblib
3. Run Jupyter Notebook
jupyter notebook

Open the notebook and run the cells step by step.

---
## Future Improvements

- Hyperparameter tuning for Random Forest

- Testing advanced models such as XGBoost or LSTM

- Integrating real-time cryptocurrency APIs

- Building a dashboard for volatility monitoring

- Deploying the model as an API or web application

---
## Key Learning Outcomes

- Understanding the machine learning workflow

- Performing exploratory data analysis on financial data

- Training and evaluating regression models

- Working with time-series style dataset splits

- Saving trained models using Joblib

---
## Author

Machine Learning project focused on financial data analysis and predictive modeling.
