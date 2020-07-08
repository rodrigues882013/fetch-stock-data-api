
from flask import request, jsonify, Blueprint, current_app as app
from fetch_stock_data_api.auth.service import requires_auth
from flask_restful import Resource, Api

from fetch_stock_data_api.decorators import logger_gunicorn
from service import StockService as service

stock_bp = Blueprint('stock_bp', __name__)
api = Api(feed_bp)


class Stock(Resource):

    @requires_auth
    @logger_gunicorn
    def get(self, stock_id):
        try:
            app.logger.info("Retrieve stock info from: %s", stock_id)
            result = service.fetch_data(stock_id)
            app.logger.info("Stock info retrived from: %s, result: %s", stock_id, result)
            return result

        except e as Exception:
            app.logger.error("Error to retrive info from: %s, error: %s", stock_id, error)
            return jsonify(dict(message='Error on retry information')), 500



api.add_resource(Feed, '/stock/<stock_id>')
