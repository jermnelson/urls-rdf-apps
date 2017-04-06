from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
pages = FlatPages(app)
presentation = sorted(pages, key=lambda p: p.meta['order'])

@app.route("/")
def index():
    return render_template("urls-rdf-apps/index.html",
        category='home',
        presentation=presentation)

@app.route("/<path:path>/")
def page(path):
    prev_page, next_page = None, None
    page = pages.get_or_404(path)
    if page.meta.get('order')-1 > -1:
        prev_page = presentation[page.meta.get('order')-1]
    if page.meta.get('order') + 1 < len(presentation):
        next_page = presentation[page.meta.get('order')+1]
    return render_template("urls-rdf-apps/page.html",
        page=page,
        category='pages',
        presentation=presentation,
        previous_page=prev_page,
        next_page=next_page)
