from Photisc import app
from flask import render_template
import make_content

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/select_template')
def select_template():
    template_datas = [
        {'image':"images/no_image.png",
        'description':"テスト用1",
        'link_num':1,
        'last_updated':"2022年1月7日"},

        {'image':"images/no_image.png",
        'description':"テスト用2",
        'link_num':2,
        'last_updated':"2022年1月7日"}
    ]
    return render_template(
        "select_template.html",
        template_datas = template_datas
        )

@app.route('/template/temp1')
def temp1():
    return render_template("template/temp1.html")

@app.route('/template/temp2')
def temp2():
    return render_template("template/temp2.html")

@app.route('/404')
def page404():
    return render_template("404.html")
