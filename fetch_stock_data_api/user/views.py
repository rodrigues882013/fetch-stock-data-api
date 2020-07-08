from flask import request, jsonify, Blueprint, current_app as app
from fetch_stock_data_api.auth.service import requires_auth
from flask_restful import Resource, Api

from fetch_stock_data_api.decorators import logger_gunicorn
from service import UserService as service

user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)


class User(Resource):

    @requires_auth
    @logger_gunicorn
    def get(self, id):
        app.logger.info("Getting user with id: %s", id)
        return jsonify(service.find_one(id))

    @requires_auth
    @logger_gunicorn
    def put(self, id):
        app.logger.info("Updating user with id: %s", id)
        return jsonify(service.update(request, id)), 200


api.add_resource(User, '/users/<int:id>')
