import os
from requests import get
from datetime import datetime, timezone, timedelta
from flask import current_app as app

url = os.getenv('FETCH_STOCK_DATA_API_URL')

def __to_timestamp(date):
    dt = datetime.strptime(date + ' 00:00:00', '%Y-%m-%d %H:%M:%S') 
    return dt.replace(tzinfo=timezone.utc).timestamp()

def __add_one_day(date):
    dt = datetime.strptime(date + ' 00:00:00', '%Y-%m-%d %H:%M:%S') 
    return (dt + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

def __format_url(stock_id, date):
    return '{url}/finance/chart/{stock_id}?period1={date_1}&period2={date_2}&interval=1d&includePrePost=prepost&events=div,splits'.format(
        url=url,
        stock_id=stock_id,
        date_1=int(__to_timestamp(date)), 
        date_2=int(__to_timestamp(__add_one_day(date)))
    )
    
def fetch_data(stock_id, stock_bought_at, stock_sold_at):

    if url is None:
        raise AttributeError('url is null')

    data_from_bought, data_from_sold = get(__format_url(stock_id, stock_bought_at)), get(__format_url(stock_id, stock_sold_at))

    if data_from_bought.status_code == 200 and data_from_sold.status_code == 200:
        return dict(
            data_from_bought=data_from_bought.content,
            data_from_sold=data_from_sold.content)

    