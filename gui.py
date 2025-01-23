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
            soil_numeric = soil_mapping.get(soil_type, -1)  # Default to -1 for invalid inputs

            # Validate soil_numeric
            if soil_numeric == -1:
                raise ValueError("Invalid soil type selected.")

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

    # Set the size of the GUI window (Width x Height)
    window_width, window_height = 500, 400
    root.geometry(f"{window_width}x{window_height}")

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = (screen_height // 2) - (window_height // 2)
    position_right = (screen_width // 2) - (window_width // 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a frame to center all widgets
    frame = tk.Frame(root)
    frame.pack(expand=True)  # Center the frame in the window

    # Add form widgets inside the frame
    tk.Label(frame, text="Temperature:").grid(row=0, column=0, padx=5, pady=5)
    temp_entry = tk.Entry(frame)
    temp_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Humidity:").grid(row=1, column=0, padx=5, pady=5)
    humid_entry = tk.Entry(frame)
    humid_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Moisture:").grid(row=2, column=0, padx=5, pady=5)
    moist_entry = tk.Entry(frame)
    moist_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame, text="Nitrogen:").grid(row=3, column=0, padx=5, pady=5)
    nitrogen_entry = tk.Entry(frame)
    nitrogen_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame, text="Potassium:").grid(row=4, column=0, padx=5, pady=5)
    potassium_entry = tk.Entry(frame)
    potassium_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(frame, text="Phosphorous:").grid(row=5, column=0, padx=5, pady=5)
    phosphorous_entry = tk.Entry(frame)
    phosphorous_entry.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(frame, text="Soil Type:").grid(row=6, column=0, padx=5, pady=5)
    soil_type_var = tk.StringVar(frame)
    soil_type_var.set("Select Soil Type")
    soil_type_dropdown = tk.OptionMenu(frame, soil_type_var, "Sandy", "Loamy", "Black", "Red", "Clayey")
    soil_type_dropdown.grid(row=6, column=1, padx=5, pady=5)

    predict_button = tk.Button(frame, text="Predict", command=predict_action)
    predict_button.grid(row=7, columnspan=2, pady=10)

    result_label = tk.Label(frame, text="", font=("Helvetica", 14))
    result_label.grid(row=8, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
