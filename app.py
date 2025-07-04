import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('best_model.pkl', 'rb'))

st.title("🌧️ Rainfall Prediction App")
st.write("Enter weather details to predict if it will rain tomorrow.")

# Example fields - adjust to your dataset
year = st.number_input("Year", min_value=2000, max_value=2050, value=2024)
month = st.number_input("Month", min_value=1, max_value=12, value=7)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
wind = st.number_input("Wind Speed (km/h)")

features = np.array([[year, month, temperature, humidity, wind]])

if st.button("Predict"):
    prediction = model.predict(features)
    st.success("☔ Rain Expected" if prediction[0] == 1 else "🌤️ No Rain")
