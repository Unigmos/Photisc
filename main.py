from Photisc import app
from flask import render_template

@app.route('/')
def index():
    data = {
        'title': 1,
        'price': 1200,
        'other': "発売停止"}
    return render_template(
        "index.html",
        data = data)

@app.route('/select_template')
def select_template():
    return render_template("select_template.html")