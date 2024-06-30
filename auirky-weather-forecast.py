import tkinter as tk
import random

class WeatherForecastApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quirky Weather Forecast Generator")
        
        
        self.root.configure(bg='skyblue')
        
        self.weather_conditions = [
            "Sunny with a chance of meatballs",
            "Snowing candy canes",
            "Thunderstorms with a side of spaghetti",
            "Rain of gummy bears",
            "Cloudy with cotton candy",
            "Hailstorm of marshmallows",
            "Partly cloudy with flying pigs",
            "it might be rain in noon",
            "probably the sunrises after 10 am",
            "Clear skies but watch out for UFOs"
        ]
        
        self.title_label = tk.Label(root, text="Welcome to the Quirky Weather Forecast!", font=("Helvetica", 16), bg='skyblue')
        self.title_label.pack(pady=20)
        
        self.generate_button = tk.Button(root, text="Generate Forecast", command=self.generate_forecast, font=("Helvetica", 14))
        self.generate_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg='blue')
        self.result_label.pack(pady=20)
        
    def generate_forecast(self):
        forecast = random.choice(self.weather_conditions)
        self.result_label.config(text=forecast)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherForecastApp(root)
    root.mainloop()