import re
from functools import wraps
from operator import itemgetter
from .exceptions import BadRequestException
from flask import request, current_app as app
from datetime import datetime



def valid(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        params = request.get_json()
        stock_id = params.get('stock_id') 
        stock_bought_at = params.get('stock_bought_at')
        stock_sold_at = params.get('stock_sold_at')
        quantity = params.get('quantity')
        is_real_state_stock = params.get('is_real_state_stock')
        
        if not stock_id:
            raise BadRequestException('stock_id cannot be empty or null')

        if not stock_bought_at:
            raise BadRequestException('stock_bought_at cannot be empty or null')
        else:
            try:
                datetime.strptime(stock_bought_at,'%Y-%m-%d')
            except:
                raise BadRequestException('stock_bought_at is an invalid format')

        if not stock_sold_at:
            raise BadRequestException('stock_sold_at cannot be empty or null')
        else:
            try:
                datetime.strptime(stock_sold_at,'%Y-%m-%d')
            except:
                raise BadRequestException('stock_sold_at is an invalid format')
        
        if not quantity:
            raise BadRequestException('quantity cannot be empty or null')
        elif not isinstance(quantity, int):
            raise BadRequestException('quantity is an invalid format')

        if is_real_state_stock is None:
            raise BadRequestException('is_real_state_stock cannot be empty or null')
        elif not isinstance(is_real_state_stock, bool):
            raise BadRequestException('is_real_state_stock is an invalid format')

        return f(*args, **kwargs)
    return decorated
