# Model 을 만든다 -> Table 생성
# 게시글 - posts

from db import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(300),nullable=False)
    # 서버(DB)에서 생성 시점의 시간을 자동으로 기록합니다.
    created_at = db.Column(db.DateTime, server_default=db.func.now())