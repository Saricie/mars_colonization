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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
