from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def main(title):
    param = dict()
    param["title"] = title
    return render_template("base.html", **param)


@app.route('/training/<prof>')
def training(prof):
    param = dict()
    param["title"] = 'Симуляторы'
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        param["prof"] = 'Инженерные симуляторы'
    else:
        param["prof"] = 'Научные симуляторы'
    return render_template("training.html", **param)


@app.route("/list_prof/<profs_list>")
def list_prof(profs_list):
    param = dict()
    param["title"] = 'Профессии'
    if profs_list == "ol":
        param["list"] = "ol"
    elif profs_list == "ul":
        param["list"] = "ul"
    return render_template("list_prof.html", **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
