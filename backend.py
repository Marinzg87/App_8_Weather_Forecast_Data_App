import os
import requests

API_KEY = os.getenv("OPEN_WEATHER_API")


def get_data(place, days=None, option=None):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    if option == "Temperature":
        filtered_data = [dict["main"]['temp'] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
