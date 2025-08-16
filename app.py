import streamlit as st
import numpy as np
import pickle

# Load model and scalers
model = pickle.load(open('model (1).pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
ms = pickle.load(open('minmaxscaler.pkl','rb'))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Streamlit UI
st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and weather conditions to get the best crop suggestion.")

# Input fields
N = st.number_input("Nitrogen", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus", min_value=0.0, step=1.0)
K = st.number_input("Potassium", min_value=0.0, step=1.0)
temp = st.number_input("Temperature (°C)", step=0.1)
humidity = st.number_input("Humidity (%)", step=0.1)
ph = st.number_input("pH value", step=0.1)
rainfall = st.number_input("Rainfall (mm)", step=0.1)

# Predict button
if st.button("Predict Best Crop"):
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    # Apply same preprocessing
    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        st.success(f"✅ {crop} is the best crop to be cultivated in these conditions.")
    else:
        st.error("❌ Sorry, could not determine the best crop with the provided data.")
