from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello Android 5!'


if __name__ == '__main__':
    app.run()
