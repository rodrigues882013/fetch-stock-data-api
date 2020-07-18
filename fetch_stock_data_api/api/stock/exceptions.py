class BaseException(Exception):
    def __init__(self, message):
        self.__message = message
    
    @property
    def message(self):
        return self.__message

class IntegrationException(BaseException):
    def __init__(self, message):
        super().__init__(message)

class OperationExecutionException(BaseException):
    def __init__(self, message):
        super().__init__(message)

class BadRequestException(BaseException):
    def __init__(self, message):
        super().__init__(message)

class NotFoundStockException(BaseException):
    def __init__(self, message):
        super().__init__(message)