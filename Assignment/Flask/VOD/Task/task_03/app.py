from flask import Flask, render_template
from flask_smorest import Api
from db import db
from models import Post
from posts_routes import posts_blp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gsig95rp@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# bluprint 설정
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
api.register_blueprint(posts_blp)

@app.route('/manage-posts')
def manage_posts():
    return render_template('posts.html')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)