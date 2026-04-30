from datetime import datetime

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    posts = db.relationship('Post', backref='author')


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    comments = db.relationship('Comment', backref='post')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
