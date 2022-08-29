from flask import Blueprint, render_template

from blog.db import PostDB

blog_router = Blueprint('blog', __name__)
db = PostDB()


@blog_router.route('/')
def index():
    return render_template('index.html')


@blog_router.route('/posts')
def get_posts():
    posts = db.get_all()
    return render_template('posts.html', posts=posts)


@blog_router.route('/posts/<int:id_>')
def get_post(id_):
    post = db.get_one(id_)
    return render_template('post.html', post=post)
