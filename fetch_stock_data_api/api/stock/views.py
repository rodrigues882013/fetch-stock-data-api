
from flask import request, jsonify, Blueprint, current_app as app
from api.auth.service import requires_auth
from flask_restful import Resource, Api

from api.decorators import logger_gunicorn
from .service import fetch_data

stock_bp = Blueprint('stock_bp', __name__)
api = Api(stock_bp)


class Stock(Resource):

    @requires_auth
    @logger_gunicorn
    def get(self, stock_id):
        try:
            app.logger.info("Retrieve stock info from: %s", stock_id)
            result = fetch_data(stock_id, request.args['stock_bought_at'], request.args['stock_sold_at'])
            app.logger.info("Stock info retrived from: %s, result: %s", stock_id, result)
            return result

        except Exception as e:
            app.logger.error("Info retrieve error from: %s, error: %s", stock_id, e)
            return jsonify(dict(message='Error on retry information')), 400



api.add_resource(Stock, '/stock/<stock_id>')
