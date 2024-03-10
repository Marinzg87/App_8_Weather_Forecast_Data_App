import os
import requests

API_KEY = os.getenv("OPEN_WEATHER_API")


def get_data(place, days=None):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=2))
