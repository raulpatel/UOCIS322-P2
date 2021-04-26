"""
John Doe's Flask API.
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker test!\n"

@app.route("/hello")
def new():
    return "Hello there friend.\n"

@app.route("/<path:name>")
def page_render(name):
    parts = name.split('.')
    if parts[-1] != "html" or parts[-1] != "css":
        abort(403)
    try:
        with open(name, "r") as f:
            pass
    except FileNotFoundError:
        abort(404)
    return render_template(name)

@app.errorhandler(404)
def error_404():
    return render_template("404.html")

@app.errorhandler(403)
def error_404():
    return render_template("403.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
