
🪙 Cryptocurrency Volatility Prediction
A robust machine learning project focused on analyzing and forecasting the price fluctuations of diverse digital assets using historical market data.

📋 Project Overview
This project processes a large-scale financial dataset to predict cryptocurrency volatility. By calculating price spreads and normalizing market features, it provides a foundation for identifying risk patterns in over 56 different cryptocurrencies, including Bitcoin, Litecoin, and XRP.

🛠️ Tech Stack
Data Processing: Pandas, NumPy

Machine Learning: Scikit-Learn

Model Persistence: Joblib

Development Environment: Jupyter Notebook / Google Colab

📊 Dataset & Feature Engineering
The model is trained on a dataset containing 72,946 entries with the following key features:

Market Basics: Open, Close, High, Low, and Volume.

Market Cap: Total valuation of the asset at the time of recording.

Engineered Feature (Volatility): A custom metric calculated as:
Volatility = (High - Low) / Open

⚙️ Development Workflow
1. Data Cleaning & Preprocessing 🧹
Column Reduction: Dropped Unnamed: 0 as it was redundant for modeling.

Temporal Optimization: Removed timestamp while retaining the date column to simplify the dataset without losing historical context.

Missing Value Management: Performed checks for null values to ensure data integrity.

2. Feature Scaling ⚖️
Utilized Scikit-Learn's scaling tools to normalize features, ensuring that high-value metrics (like Market Cap) do not disproportionately influence the model compared to smaller metrics (like price).

3. Model Training & Export 💾
Implemented a predictive model to target the engineered volatility metric.

Persistent Storage:

crypto_model.pkl: The trained predictive model.

scaler.pkl: The exact scaling parameters used during training, essential for accurate real-world deployment.

🚀 How to Use
Clone the Repository:

Bash
git clone https://github.com/yourusername/crypto-volatility-prediction.git
Install Dependencies:

Bash
pip install pandas numpy scikit-learn joblib
Run the Analysis: Open the .ipynb file in Jupyter or Google Colab to see the full training pipeline.
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

**Last Updated**: March 2026
