
# 🌦 Weather App

**Created by Uday Bhasker and Srinivas Naren**

A **simple and interactive Weather App** built in Python using **Tkinter** for GUI and **OpenWeatherMap API** for real-time weather data. Users can search for **any city worldwide**, choose **Celsius or Fahrenheit**, and get **current weather information** like temperature, humidity, wind, and condition.

---

## **Features**

* ✅ Search **any city worldwide**.
* ✅ **Multiple city matches handled** automatically.
* ✅ Choose **Celsius or Fahrenheit**.
* ✅ Simple, clean, and **portfolio-ready GUI**.
* ✅ Displays **city, temperature, feels like, condition, humidity, and wind**.

---

## **Demo**

Here’s how the app looks:

![Weather App Demo](demo.gif)
*GIF shows entering a city, selecting units, and getting weather.*

> Click the button below to **download and run the app**:

[Download Weather App](WeatherApp.zip)

> **Note:** You need Python installed to run the `.py` file.
> Or, if you create an `.exe` using **PyInstaller**, Windows users can run it directly.

---

## **Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/YourUsername/WeatherApp.git
cd WeatherApp
```

2. **Install dependencies:**

```bash
pip install requests
```

3. **Run the app:**

```bash
python app.py
```

---

## **Project Structure**

```
WeatherApp/
│
├─ app.py                # Main Python GUI code
├─ README.md             # This file
├─ requirements.txt      # Optional: list of dependencies
└─ demo.gif              # GIF showing the app in action
```

---

## **Usage**

1. Enter a **city name** in the input box.
2. If multiple cities match, choose the correct one from the pop-up.
3. Select your **preferred temperature unit (C/F)**.
4. Click **Get Weather** to see the current weather information.

---

## **How It Works**

1. **Geocoding API:** Converts city name → latitude/longitude.
2. **Weather API:** Gets real-time weather data using coordinates.
3. **GUI Display:** Shows weather info in a **neat, readable format**.

---

## **Technologies Used**

* **Python 3**
* **Tkinter** (GUI)
* **Requests** (API calls)
* **OpenWeatherMap API**

---

## **Credits**

* **Uday Bhasker** – Co-developer
* **Srinivas Naren** – Developer

---
