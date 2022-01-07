from Photisc import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/select_template')
def select_template():
    template_data = [
        {'image':"images/no_image.png",
        'description':"テスト用1",
        'last-updated':"2022年1月7日"},

        {'image':"images/no_image.png",
        'description':"テスト用2",
        'last-updatd':"2022年1月7日"}
    ]
    return render_template(
        "select_template.html",
        template_data = template_data
        )
