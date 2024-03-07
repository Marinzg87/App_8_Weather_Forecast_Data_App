import os
import requests

API_KEY = os.environ('API_OPENWEATHERMAP')


def get_data(place, days=None, option=None):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
