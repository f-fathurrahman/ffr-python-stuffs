from flask import Flask, render_template, request, send_from_directory, url_for
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def handle_root():
    return render_template("test_upload.html")

@app.route("/test_upload", methods=["GET", "POST"])
def handle_upload():
    if request.method == "POST":
        f = request.files["file_gambar"]
        fnamesaved = "static/" + secure_filename(f.filename)
        f.save(fnamesaved)

        response_str = """
        <html>
        <body>
        <img src="{}" />
        </body>
        </html>
        """.format(fnamesaved)

        return response_str

if __name__ == "__main__":
    app.run(debug=True)

