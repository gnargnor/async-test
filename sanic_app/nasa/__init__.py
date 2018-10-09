import os
import grequests
import requests
import math
from tqdm import tqdm

NASA_API_KEY = os.environ['NASA_API_KEY']


def make_date_url(date):
    return f'https://api.nasa.gov/EPIC/api/enhanced/date/{date}?api_key={NASA_API_KEY}'


def make_url_list(dates):
    urls = [make_date_url(date) for date in dates]
    return urls


def lookup_all_epic_dates(urls):
    print(urls[0])
    print(requests.get(urls[0]))
    total = len(urls)
    print(range(math.floor(len(urls) / 10)))
    pbar = tqdm(total=total)
    responses = []
    for i in range(11):
        print(i * math.floor(len(urls) / 10) + (len(urls) - i * math.floor(len(urls) / 10)) if i != 10 else i * math.floor(len(urls) / 10) + (len(urls) - i * math.floor(len(urls) / 10)))
        mini_list = urls[i:(i * math.floor(len(urls) / 10) + (len(urls) - i * math.floor(len(urls) / 10)) if i != 10 else i * math.floor(len(urls) / 10) + (len(urls) - i * math.floor(len(urls) / 10)))]
        rs = (grequests.get(u) for u in mini_list)
        responses.append(grequests.map(rs))
        pbar.update(math.floor(len(urls) / 10))
    pbar.close()
    print(responses)


def make_date_list(date_object_list):
    dates = [date_object['date'] for date_object in date_object_list]
    return dates


def get_all_epic_urls():
    response = requests.get(f'https://api.nasa.gov/EPIC/api/enhanced/all?api_key={NASA_API_KEY}')
    print(response.status_code)
    dates = make_date_list(response.json())
    urls = make_url_list(dates)
    print(urls)
    return urls