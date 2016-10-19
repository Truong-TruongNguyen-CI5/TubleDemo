import json
from flask import Flask, request

app = Flask(__name__)

post1 = {
    "title" : "Good day",
    "content" : "Today i met a girl"
}

post2 = {
    "title" : "Bad day",
    "content" : "Today i met a gay"
}

posts = [post1, post2]

print(post1["title"])

@app.route('/')
def hello_world():

    return json.dumps(posts)

@app.route('/addpost', methods=["POST"])
def add_post():
    args = request.form
    title = args["title"]
    content = args["content"]
    new_post = {"title": title,
                "content": content
                }
    posts.append(new_post)
    print(title, content)
    return "OK"


if __name__ == '__main__':
    app.run()
