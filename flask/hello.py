from flask import Flask

app = Flask(__name__)

@app.route("/test/")
def hello():
    return "Hello from route /test"

@app.route("/")
def hello_root():
    return "Hello from route / "

if __name__ == "__main__":
    app.run()

