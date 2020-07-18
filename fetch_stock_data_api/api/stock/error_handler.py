from functools import wraps
from flask import current_app as app

from .exceptions import IntegrationException, OperationExecutionException, BadRequestException, NotFoundStockException


def error_handler(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)

        except IntegrationException as e:
            app.logger.error(f'External API communication error, data: {kwargs}, error: {e}')
            return dict(message=e.message), 504

        except OperationExecutionException as e:
            app.logger.error(
                f'Something goes wrong on process your request, reviewed and try again,  data: {kwargs}, error: {e}')
            return dict(message='Something goes wrong on process your request, reviewed and try again'), 400

        except BadRequestException as e:
            app.logger.error(
                f'There is invalid parameter on your data, reviewd and try again,  data: {kwargs}, error: {e}')
            return dict(message=e.message), 400
        
        except NotFoundStockException as e:
            app.logger.error(
                f'This stock wasnt found,  data: {kwargs}, error: {e}')
            return dict(message=e.message), 404

        except Exception as e:
            app.logger.error(f'Unknown server error,  data: {kwargs}, error: {e}')
            return dict(message='Unknown server error'), 500

    return decorated
