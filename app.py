from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
# db = SQLAlchemy(app)

# class ItemPost(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title=db.Column(db.String(100))
#     content=db.Column(db.Text)
#     seller=db.Column(db.String(30))
#     date_posted=db.column(db.DateTime)

#     def __repr__(self):
#         return 'Blog Post' + str(self.id)

all_posts=[
    {     
          'author':'jim',
          'title':'Post 1',
          'content':'content of post 1',
          'date_posted':'April 20,2020', 
          'price':'₹10,999'

    },
    {
          'author':'kevin',
          'title':'Post 2',
          'content':'content of post 2', 
          'date_posted':'April 21,2020',
          'price':'₹11,999'
    }

]


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html',posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)