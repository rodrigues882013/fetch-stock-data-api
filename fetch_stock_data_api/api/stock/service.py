from datetime import datetime, timezone, timedelta
from .api import fetch


def __to_timestamp(date):
    dt = datetime.strptime(f'{date} 00:00:00', '%Y-%m-%d %H:%M:%S')
    return dt.replace(tzinfo=timezone.utc).timestamp()


def __add_one_day(date):
    dt = datetime.strptime(f'{date} 00:00:00', '%Y-%m-%d %H:%M:%S')
    return (dt + timedelta(days=1)).strftime('%Y-%m-%d')


def fetch_data(stock_id, date):
    date_in_timestamp = __to_timestamp(date)
    date_upper_bound_in_timestamp = __to_timestamp(__add_one_day(date))
    return fetch(stock_id, date_in_timestamp, date_upper_bound_in_timestamp)


def execute_tax_calculation(data_bought, data_sold):
    return ""
