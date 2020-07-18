from flask import request, Blueprint, current_app as app
from api.auth.service import requires_auth
from flask_restful import Resource, Api

from api.decorators import logger_gunicorn
from .error_handler import error_handler
from .service import fetch_data, execute_tax_calculation

stock_bp = Blueprint('stock_bp', __name__)
api = Api(stock_bp)


class Stock(Resource):
    
    @requires_auth
    @logger_gunicorn
    @error_handler
    def get(self, stock_id):
        app.logger.info(f'Retrieve stock info from: {stock_id}')
        stock_data_bought = fetch_data(stock_id, request.args['stock_bought_at'])
        stock_data_sold = fetch_data(stock_id, request.args['stock_sold_at'])
        result = execute_tax_calculation(stock_data_bought, stock_data_sold)
        app.logger.info(f'Stock info retrieved from: {stock_id}, result: {result}')
        return result


api.add_resource(Stock, '/stock/<stock_id>')
