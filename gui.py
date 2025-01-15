import tkinter as tk
from tkinter import messagebox
from model_prediction import predict_fertilizer

def run_gui():
    print("Running GUI...")  # Added print statement for verification
    
    def predict_action():
        try:
            # Collect input values from user
            temperature = float(temp_entry.get())
            humidity = float(humid_entry.get())
            moisture = float(moist_entry.get())
            nitrogen = float(nitrogen_entry.get())
            potassium = float(potassium_entry.get())
            phosphorous = float(phosphorous_entry.get())
            soil_type = soil_type_var.get()

            # Map soil type to numeric value
            soil_mapping = {"Sandy": 0, "Loamy": 1, "Black": 2, "Red": 3, "Clayey": 4}
            soil_numeric = soil_mapping[soil_type]

            # Make prediction
            features = [temperature, humidity, moisture, nitrogen, potassium, phosphorous, soil_numeric]
            result = predict_fertilizer(features)

            # Display result
            result_label.config(text=f"Predicted Crop Type: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")

    # Set up the GUI
    root = tk.Tk()
    root.title("Fertilizer Impact Prediction")

    tk.Label(root, text="Temperature:").grid(row=0, column=0)
    temp_entry = tk.Entry(root)
    temp_entry.grid(row=0, column=1)

    tk.Label(root, text="Humidity:").grid(row=1, column=0)
    humid_entry = tk.Entry(root)
    humid_entry.grid(row=1, column=1)

    tk.Label(root, text="Moisture:").grid(row=2, column=0)
    moist_entry = tk.Entry(root)
    moist_entry.grid(row=2, column=1)

    tk.Label(root, text="Nitrogen:").grid(row=3, column=0)
    nitrogen_entry = tk.Entry(root)
    nitrogen_entry.grid(row=3, column=1)

    tk.Label(root, text="Potassium:").grid(row=4, column=0)
    potassium_entry = tk.Entry(root)
    potassium_entry.grid(row=4, column=1)

    tk.Label(root, text="Phosphorous:").grid(row=5, column=0)
    phosphorous_entry = tk.Entry(root)
    phosphorous_entry.grid(row=5, column=1)

    tk.Label(root, text="Soil Type:").grid(row=6, column=0)
    soil_type_var = tk.StringVar(value="Sandy")
    tk.OptionMenu(root, soil_type_var, "Sandy", "Loamy", "Black", "Red", "Clayey").grid(row=6, column=1)

    tk.Button(root, text="Predict", command=predict_action).grid(row=7, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=8, column=0, columnspan=2)

    root.mainloop()

# Uncomment below to test the GUI when you call this script
# run_gui()
