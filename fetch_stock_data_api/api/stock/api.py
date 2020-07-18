import os
from requests import get
from flask import current_app as app
from .exceptions import NotFoundStockException, IntegrationException
from json import load

base_url = os.getenv('FETCH_STOCK_DATA_API_URL')

def fetch(stock_id, date_1, date_2):
    if base_url is None:
        raise AttributeError('url is null')

    try:
        result = get(
            f'{base_url}/{stock_id}.SA?period1={int(date_1)}&period2={int(date_2)}&interval=1d&includePrePost=prepost&events=div,splits')
    except Exception as e:
        app.logger.error(f'Error external API call: {e}')
        raise IntegrationException('External API communication error')
    
    if result.status_code == 200:
        return result.json()
    elif result.status_code == 404:
        raise NotFoundStockException(f'Stock: {stock_id} was not found')
