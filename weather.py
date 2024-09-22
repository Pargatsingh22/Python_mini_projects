import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cb0530d7a9e4f4ce94e8a6860197a2ea'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {int(main['temp'])}°C")
        print(f"Weather: {weather['description']}")
    else:
        print(f"City {city} not found.")

city = input("Enter city name: ")
get_weather(city)