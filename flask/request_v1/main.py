# This is adapted from:
#
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

from flask import Flask, request

app = Flask(__name__)


# Example url
# htpp://127.0.0.1/request-example?arg1=val1&arg2=val2
#
@app.route("/query-example")
def query_example():
    
    language = request.args.get("language")
    framework = request.args.get("framework")
    website = request.args.get("website")
    
    response_str = """
    <html>

    <head>
    <title>Testing flask.request</title>
    </head>

    <body>
    <p>The language is {}.</p>
    <p>The framework is {}.</p>
    <p>The website is {}.</p>
    </body>
    </html>
    """.format(language, framework, website)

    return response_str


@app.route("/form-example", methods=["GET", "POST"])
def form_example():
    #
    if request.method == "POST":
        language = request.form.get("language")
        framework = request.form.get("framework")
        response_str = """
        The language is {}.<br>
        The framework is {}.<br>
        """.format(language, framework)
        return response_str
    
    # no need to use else:
    response_str = """
    <form method="POST">
    Language: <input type="text" name="language"><br>
    Framework: <input type="text" name="framework"><br>
    <input type="submit" value="Submit now"><br>
    </form>
    """

    return response_str

@app.route("/json-example", methods=["POST"])
def json_example():
    req_data = request.get_json()

    language = req_data["language"]
    framework = req_data["framework"]
    python_version = req_data["version_info"]["python"]
    example = req_data["examples"][0]
    boolean_test = req_data["boolean_test"]

    response_str = """
    The language is: {}.
    The framework is: {}.
    python_version is: {}.
    example is: {}.
    boolean_test is: {}.
    """.format(language, framework, python_version, example, boolean_test)
    
    return response_str

if __name__ == "__main__":
    app.run(debug=True, port=5000)

