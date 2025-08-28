import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

API_KEY = "fc2b5e62721e5f792d74f3ec17bcd779"

def get_city_location(city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_weather(lat, lon, units="metric"):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={API_KEY}"
    return requests.get(url).json()

def fetch_weather():
    city_input = city_entry.get().strip()
    if not city_input:
        messagebox.showerror("Error", "Please enter a city name")
        return

    locations = get_city_location(city_input)
    if not locations:
        messagebox.showerror("Error", "City not found!")
        return

    if len(locations) > 1:
        city_names = [f"{loc['name']}, {loc.get('state','')}, {loc['country']}" for loc in locations]
        choice = simpledialog.askinteger("Choose City",
                                         "Multiple cities found:\n" + "\n".join(f"{i+1}. {name}" for i, name in enumerate(city_names)) + "\nEnter number:")
        if not choice or choice < 1 or choice > len(locations):
            messagebox.showerror("Error", "Invalid choice!")
            return
        city = locations[choice - 1]
    else:
        city = locations[0]

    lat, lon = city["lat"], city["lon"]
    units_input = unit_var.get()
    units = "metric" if units_input == "C" else "imperial"

    weather = get_weather(lat, lon, units)
    if weather.get("cod") != 200:
        messagebox.showerror("Error", "Failed to fetch weather!")
        return

    temp = weather['main']['temp']
    feels_like = weather['main']['feels_like']
    condition = weather['weather'][0]['description']
    humidity = weather['main']['humidity']
    wind = weather['wind']['speed']

    result_label.config(
        text=f"City: {city['name']}, {city['country']}\n"
             f"Temp: {temp}°\n"
             f"Feels Like: {feels_like}°\n"
             f"Condition: {condition.title()}\n"
             f"Humidity: {humidity}%\n"
             f"Wind: {wind} m/s"
    )

# --- GUI ---
root = tk.Tk()
root.title("Weather App")
root.geometry("400x330")  # increased height for footer

tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

city_entry = tk.Entry(frame, width=25, font=("Helvetica", 12))
city_entry.pack(side="left", padx=5)

tk.Button(frame, text="Get Weather", command=fetch_weather).pack(side="left")

# Units
unit_var = tk.StringVar(value="C")
unit_frame = tk.Frame(root)
unit_frame.pack(pady=5)
tk.Radiobutton(unit_frame, text="Celsius", variable=unit_var, value="C").pack(side="left", padx=5)
tk.Radiobutton(unit_frame, text="Fahrenheit", variable=unit_var, value="F").pack(side="left", padx=5)

# Result
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left", wraplength=380)
result_label.pack(pady=10)

# Footer (move it before mainloop)
tk.Label(root, text="Created by Uday Bhasker and Srinivas Naren", font=("Helvetica", 10, "italic")).pack(side="bottom", pady=5)

root.mainloop()
