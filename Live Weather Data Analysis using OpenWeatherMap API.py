import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
cities = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", "Pune", "Hyderabad"]

weather_data = []

for city in cities:
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_data.append({
            'City': city,
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather': data['weather'][0]['main']
        })
    else:
        print(f"❌ Failed to fetch weather for {city} (Status Code: {response.status_code})")

df = pd.DataFrame(weather_data)
print("\n📊 Weather Data:\n", df)

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm")
plt.title("City-wise Temperature")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Humidity (%)", data=df, palette="Blues")
plt.title("City-wise Humidity")
plt.tight_layout()
plt.show()



