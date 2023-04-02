from flask import jsonify
from adv import get_app

app = get_app()


class ApiException(Exception):

    def __init__(self, status_code: int, description):
        self.status_code = status_code
        self.description = description


@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({'status': 'error', 'description': error.description})
    response.status_code = error.status_code
    return response
