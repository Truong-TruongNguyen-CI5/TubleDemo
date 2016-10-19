import json
from flask import Flask

app = Flask(__name__)

post1 = {
    "title" : "Good day",
    "content" : "Today i met a girl"
}

@app.route('/')
def hello_world():
    return json.dumps(post1)


if __name__ == '__main__':
    app.run()
