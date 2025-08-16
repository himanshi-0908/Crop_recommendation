# 🌾 Crop Yield Prediction

This project uses **Machine Learning** to recommend the most suitable crop for cultivation based on soil and environmental conditions.

---

## 📌 Features
- Predicts the best crop to grow using input parameters:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature 🌡️
  - Humidity 💧
  - pH value ⚗️
  - Rainfall 🌧️
- Trained on the **Crop Recommendation Dataset**.
- Web app interface built using **Streamlit**.
- Can be deployed on **Render** / **Streamlit Cloud**.

---

## 🚀 Tech Stack
- **Python**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-Learn**
- **Streamlit** (for web app)
  

---

## 📂 Project Structure
Crop_recommendation/
│-- app.py # Streamlit web app
│-- model.pkl # Trained ML model
│-- Crop_recommendation.csv # Dataset
│-- requirements.txt # Dependencies
│-- README.md # Project documentation

---

## ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Crop_recommendation.git
   cd Crop_recommendation

2. Install dependencies:

   pip install -r requirements.txt


3. Run locally:

   streamlit run app.py


4. Open the app in browser at:

   http://localhost:8501
Deployment link: https://croprecommendation1.streamlit.app/

