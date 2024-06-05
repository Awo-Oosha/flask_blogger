from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

# Jinja filters
# safe
# capitalize
# lower
# upper
# title
# trim
# striptages

# Create a route decorator

@app.route("/")
def index():
    first_name = "Timileyin"
    return render_template("index.html", first_name=first_name)
# def index():
#     return "<h1>Hello World<h1>"


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
    # return "<h1>Hello {}<h1>".format(name)


# Create Custom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500