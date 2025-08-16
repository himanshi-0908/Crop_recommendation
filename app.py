import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Crop dictionary
crop_dict = {
    0: "Rice", 1: "Maize", 2: "Chickpea", 3: "Kidney Beans",
    4: "Pigeon Peas", 5: "Moth Beans", 6: "Mung Bean", 7: "Black Gram",
    8: "Lentil", 9: "Pomegranate", 10: "Banana", 11: "Mango",
    12: "Grapes", 13: "Watermelon", 14: "Muskmelon", 15: "Apple",
    16: "Orange", 17: "Papaya", 18: "Coconut", 19: "Cotton",
    20: "Jute", 21: "Coffee"
}

# Page Config
st.set_page_config(page_title="🌾 Crop Recommendation", layout="centered")

# Title
st.markdown("<h2 style='text-align:center; color:green;'>🌱 Crop Recommendation System</h2>", unsafe_allow_html=True)

st.write("Enter the soil and weather conditions below to get the best crop recommendation:")

# Input fields in 2 columns
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("🌿 Nitrogen", min_value=0)
    P = st.number_input("🌿 Phosphorus", min_value=0)
    K = st.number_input("🌿 Potassium", min_value=0)
    temperature = st.number_input("🌡️ Temperature (°C)")

with col2:
    humidity = st.number_input("💧 Humidity (%)")
    ph = st.number_input("⚖️ pH Value")
    rainfall = st.number_input("🌧️ Rainfall (mm)")

# Prediction button
if st.button("🔍 Predict Crop"):
    data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(data)[0]
    crop_name = crop_dict[prediction]
    st.success(f"✅ Recommended Crop: **{crop_name}**")
