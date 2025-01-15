import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pickle

# Load dataset
data = pd.read_csv('data/fertilizer_Prediction.csv')
print("Dataset Overview:")
print(data.head())
print("\nDataset Information:")
print(data.info())

# Print actual column names to debug
print("Actual column names in the DataFrame:")
print(data.columns)

# Visualize dataset
sns.pairplot(data)
plt.show()

# Identify non-numeric columns
non_numeric_columns = data.select_dtypes(exclude=['number']).columns
print("Non-numeric columns:", non_numeric_columns)

# Convert non-numeric columns to category and then to numeric if applicable
for col in non_numeric_columns:
    # Convert to category first
    data[col] = data[col].astype('category')
    # Then convert to numeric, coercing errors to NaN
    data[col] = data[col].cat.codes  # This will convert categories to numeric codes

# Fill missing values for numeric columns
data.fillna(data.mean(), inplace=True)

# Encode categorical variables (if any remain)
data = pd.get_dummies(data, drop_first=True)  # drop_first to avoid dummy variable trap

# Print columns to debug
print("Columns in DataFrame after preprocessing:")
print(data.columns)

# Define features (X) and target variable (y)
# Assuming 'Crop Type' is the target variable; adjust as necessary
X = data.drop(columns=['Crop Type'])  # Replace 'Crop Type' with the actual target column
y = data['Crop Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate model performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the model
with open('fertilizer_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved as 'fertilizer_model.pkl'")

# Load the model
with open('fertilizer_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
print("Model loaded successfully.")

# Print the number of features the model expects
print(f"The model expects {model.n_features_in_} features.")

# Make predictions
# Create a sample input with the correct number of features
# Adjust sample_input based on the features in your dataset
# Example: [Temperature, Humidity, Moisture, Nitrogen, Potassium, Phosphorous, Soil_Type_1, Soil_Type_2, ...]
# Replace with actual feature values based on your dataset
sample_input = pd.DataFrame([[26, 52, 38, 37, 0, 0, 1, 0]], 
                             columns=X.columns)  # Ensure the DataFrame has the same columns as X

# Make prediction
prediction = loaded_model.predict(sample_input)
print(f"Predicted Crop Type: {prediction[0]}")