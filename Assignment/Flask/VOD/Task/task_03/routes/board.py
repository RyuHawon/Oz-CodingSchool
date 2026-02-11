from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')


# API List
# /board/
# 전체 게시글을 가져오는 API (GET)
# 게시글 작성 (POST)
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()

        # for board in boards:
        #     print('id', board.id)
        #     print('title', board.title)
        #     print('content', board.content)
        #     print('user_id', board.user_id)
        #     print('author_name', board.author.name)
        #     print('author_email', board.author.email)

        return jsonify([{'id':board.id, 'title':board.title, 'content':board.content, 'user_id':board.user_id, 'author_name':board.author.name, 'author_email':board.author.email}for board in boards])

    def post(self):
        pass

# # /board/<int: board_id>
# 하나의 게시글 불러오기 (GET)
# 특정 게시글 수정하기 (PUT)
# 특정 게시글 삭제하기 (DELETE)