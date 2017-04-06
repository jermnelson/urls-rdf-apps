from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
pages = FlatPages(app)

@app.route("/")
def index():
    return render_template("urls-rdf-apps/index.html",
        pages=pages)
