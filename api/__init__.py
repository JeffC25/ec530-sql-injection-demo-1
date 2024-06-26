from flask import Blueprint
from flask_restful import Api
from .resources import UserResource

api = Blueprint('api', __name__)
rest_api = Api(api)

rest_api.add_resource(UserResource, '/user')