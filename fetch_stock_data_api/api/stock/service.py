from datetime import datetime, timezone, timedelta
from .api import fetch


def __to_timestamp(date):
    dt = datetime.strptime(f'{date} 00:00:00', '%Y-%m-%d %H:%M:%S')
    return dt.replace(tzinfo=timezone.utc).timestamp()


def __add_one_day(date):
    dt = datetime.strptime(f'{date} 00:00:00', '%Y-%m-%d %H:%M:%S')
    return (dt + timedelta(days=1)).strftime('%Y-%m-%d')

def __parse_stock_result(data):
    stock_info = ((data.get('chart')).get('result')[0]).get('meta')
    return dict(price=stock_info.get('chartPreviousClose'))

def fetch_data(stock_id, date):
    date_in_timestamp = __to_timestamp(date)
    date_upper_bound_in_timestamp = __to_timestamp(__add_one_day(date))
    return __parse_stock_result(fetch(stock_id, date_in_timestamp, date_upper_bound_in_timestamp))


def execute_tax_calculation(data_bought, data_sold, quantity, is_real_state_stock):
    total_bought=data_bought.get('price') * quantity
    total_sold=data_sold.get('price') * quantity

    delta = total_bought - total_sold

    if delta < 0: # There was gain
        gain = abs(delta)

        if is_real_state_stock or gain > 20000.00:
            charged_tax = gain * 0.15005 # 15% tax + 0.005 stock_house
        else:
            charged_tax=0
    else:
        charged_tax=0
    
    return dict(charged_tax=charged_tax)
