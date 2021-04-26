"""
Raul Patel's Flask API.
"""

from flask import Flask, render_template, abort, Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker practice!\n"

@app.route("/<path:name>")
def page_render(name):
    parts = name.split('.')  # to determine extension
    if (name.count("..") or name.count("//") or name.count("~")):  # check for restricted files
        abort(403)        
    try:
        if parts[-1] == "html":  # check html file exists
            newname = "templates/" + name
            with open(newname, "r") as f:
                pass
        else:  # check non-html file exists and output content to page
            newname = "static/" + name
            with open(newname, "r") as f:
                con = f.read()
                return Response(con, mimetype='text/plain')
    except FileNotFoundError:  # file does not exist in given directories
        abort(404)
    return render_template(name)  # output html content to page  

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html")

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html") 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
