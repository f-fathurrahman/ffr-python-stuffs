from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask from ffr!'

if __name__ == '__main__':
    app.run()

