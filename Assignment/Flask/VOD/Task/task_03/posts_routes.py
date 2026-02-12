from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from models import Post

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)


posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")


@posts_blp.route("/")
class PostsList(MethodView):
    # GET 전체
    @posts_blp.response(200, PostSchema(many=True))
    def get(self):
        return Post.query.all()
    
    # POST
    @posts_blp.arguments(PostSchema)
    @posts_blp.response(201, PostSchema)
    def post(self, new_post):
        
        new_post = Post(title=new_post['title'], content=new_post['content'])
        db.session.add(new_post)
        db.session.commit()

        return new_post


@posts_blp.route("/<int:post_id>")
class PostsResource(MethodView):
    # GET 특정
    @posts_blp.response(200, PostSchema)
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post
    
    # PUT
    @posts_blp.arguments(PostSchema)
    @posts_blp.response(201, PostSchema)
    def put(self, update_post, post_id):
        post = Post.query.get_or_404(post_id)
        post.title = update_post['title']
        post.content = update_post['content']

        db.session.commit()
        return {'msg':'Successfully updated post'}
    
    @posts_blp.response(204, PostSchema)
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        
        db.session.commit()
        return {'msg':'Successfully deleted post'}