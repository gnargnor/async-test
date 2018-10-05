import os
import requests


def phone_home():
    response = requests.get(f'https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key={os.environ["NASA_API_KEY"]}')
    print(response.status_code)
    print(response.json())