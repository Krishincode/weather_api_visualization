import requests
import matplotlib.pyplot as plt

# --------------------------
# API key
API_KEY = "7d2417ff63a7e5373b6aee9bb139fd0d"   # Apni OpenWeather API key yaha daalo
# --------------------------

# Lists to store data
cities = []
temperatures = []
humidities = []
feels_like_list = []

# --------------------------
# User input for cities
print("Enter city names one by one. Type 'done' when finished:")
while True:
    city = input("City name: ")
    if city.lower() == "done":
        break
    cities.append(city)

# --------------------------
# Fetch weather data from API
for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temperatures.append(data["main"]["temp"])
        humidities.append(data["main"]["humidity"])
        feels_like_list.append(data["main"]["feels_like"])
    else:
        print(f"Data not found for {city}")
        temperatures.append(0)
        humidities.append(0)
        feels_like_list.append(0)

# --------------------------
# Visualization

# Temperature & Feels Like chart
plt.figure(figsize=(12,6))
bar_width = 0.35
x = range(len(cities))

plt.bar(x, temperatures, width=bar_width, color='orange', label='Temperature')
plt.bar([i + bar_width for i in x], feels_like_list, width=bar_width, color='red', label='Feels Like')

plt.title("Temperature & Feels Like (°C) in Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks([i + bar_width/2 for i in x], cities, rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Humidity chart
plt.figure(figsize=(12,6))
plt.bar(cities, humidities, color='blue')
plt.title("Humidity (%) in Cities")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

