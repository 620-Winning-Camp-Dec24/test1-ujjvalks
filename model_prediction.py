import pickle
import pandas as pd

# Load the trained model
with open('fertilizer_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Hello, the script has run successfully!")

def predict_fertilizer(features):
    """
    Predicts the crop type based on input features.
    :param features: A list of feature values [Temperature, Humidity, Moisture, Nitrogen, Potassium, Phosphorous, Soil Type (numeric)].
    :return: Predicted crop type.
    """
    # Convert features to DataFrame for prediction
    columns = ['Temperature', 'Humidity', 'Moisture', 'Nitrogen', 'Potassium', 'Phosphorous', 'Soil_Type']
    input_data = pd.DataFrame([features], columns=columns)

    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]
