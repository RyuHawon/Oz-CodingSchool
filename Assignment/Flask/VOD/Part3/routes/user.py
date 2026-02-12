from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from db import db
from models import User

# 스키마 정의
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/user')

# API LIST:
# (1) 전체 유저 데이터 조회 (GET)
# (2) 유저 생성 (POST)
@user_blp.route('/')
class UserList(MethodView):
    @user_blp.response(200, UserSchema(many=True))
    def get(self):
        return User.query.all()

        # user_data = [{"id":user.id, "name": user.name, "email": user.email} for user in users]
        # return jsonify(user_data)
    
    @user_blp.arguments(UserSchema)
    @user_blp.response(201, UserSchema)
    def post(self, new_user):
        print('요청은 오는가?')
        # 스키마 사용으로 바로 new_user 형태로 받을 수 있다.
        # data = request.json
        # new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return new_user

# (1) 특정 유저 데이터 조회 (GET)
# (2) 특정 유저 데이터 업데이트 (PUT)
# (3) 특정 유저 삭제 (DELETE)
@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    @user_blp.response(200, UserSchema)
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {"name": user.name, 'email': user.email}

    @user_blp.arguments(UserSchema)
    @user_blp.response(200, UserSchema)
    def put(self, user_data, user_id):
        user = User.query.get_or_404(user_id)
        # 필요없을듯
        # user_data = request.json

        user.name = user_data['name']
        user.email = user_data['email']

        db.session.commit()
        return {'msg':'Successfully updated user'}

    @user_blp.response(204)
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'msg':'Successfully deleted user'}
