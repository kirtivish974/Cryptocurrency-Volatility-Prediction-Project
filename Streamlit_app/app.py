import streamlit as st
import joblib
import numpy as np

model = joblib.load("crypto_volatility_model.pkl")

st.title("Crypto Volatility Predictor")

open_price = st.number_input("Open")
high_price = st.number_input("High")
low_price = st.number_input("Low")
close_price = st.number_input("Close")
volume = st.number_input("Volume")

ma7 = st.number_input("MA7")
ma14 = st.number_input("MA14")

price_range = st.number_input("Price Range")
price_range_pct = st.number_input("Price Range %")

returns = st.number_input("Returns")

momentum3 = st.number_input("Momentum 3")
momentum7 = st.number_input("Momentum 7")

vol_lag1 = st.number_input("Volatility Lag1")
vol_lag2 = st.number_input("Volatility Lag2")
vol_lag3 = st.number_input("Volatility Lag3")

if st.button("Predict"):

    features = np.array([[open_price,high_price,low_price,close_price,volume,
                          ma7,ma14,
                          price_range,price_range_pct,
                          returns,
                          momentum3,momentum7,
                          vol_lag1,vol_lag2,vol_lag3]])

    prediction = model.predict(features)

    st.success(f"Predicted Volatility: {prediction[0]}")