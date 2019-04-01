from flask import request
from flask_restplus import Resource

from ..model.user_dto import UserDto
from ..service.user_service import get_user, save_new_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list of registered users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return []

    @api.response(201, 'User succesfully created')
    @api.doc('Create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Created a new user"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'user id')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        """get a user by id"""
        user = get_user(id)
        if not user:
            api.abort(404)
        else:
            return user
