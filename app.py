import pickle
import numpy as np

# Load model and scalers
model = pickle.load(open('model (1).pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))

# Input values
N = 90
P = 42
k = 43
temperature = 20.879744
humidity = 82.002744
ph = 6.502985
rainfall = 202.935536

# Put values into array
input_data = np.array([[N, P, k, temperature, humidity, ph, rainfall]])

# Apply same preprocessing as training
input_data = mx.transform(input_data)
input_data = sc.transform(input_data)

# Predict
predict = model.predict(input_data)

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Get result
predict_crop_index = predict[0]
if predict_crop_index in crop_dict:
    crop = crop_dict[predict_crop_index]
    print(f"{crop} is a best crop to be cultivated")
else:
    print("Sorry, not able to recommend a proper crop for this environment")
