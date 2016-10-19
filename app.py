import json
from flask import Flask

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


if __name__ == '__main__':
    app.run()
