from flask import Flask,render_template

app=Flask(__name__)

all_posts=[
    {
          'title':'Post 1',
          'content':'content of post 1',  
    },
    {
          'title':'Post 2',
          'content':'content of post 2',  
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