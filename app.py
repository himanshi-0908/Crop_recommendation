import streamlit as st
import pickle

# Load model
model = pickle.load(open("model (1).pkl", "rb"))

st.title("Crop Recommendation System")

# Input fields
N = st.number_input("Nitrogen", min_value=0)
P = st.number_input("Phosphorus", min_value=0)
K = st.number_input("Potassium", min_value=0)
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")

if st.button("Predict Crop"):
    data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(data)[0]
    st.success(f"Recommended Crop: {prediction}")
