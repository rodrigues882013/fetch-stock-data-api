import os
from requests import get

base_url = os.getenv('FETCH_STOCK_DATA_API_URL')


def fetch(stock_id, date_1, date_2):
    if base_url is None:
        raise AttributeError('url is null')

    result = get(
        f'{base_url}/{stock_id}?period1={date_1}&period2={date_2}&interval=1d&includePrePost=prepost&events=div,splits')

    if result.status_code == 200:
        return result.content
