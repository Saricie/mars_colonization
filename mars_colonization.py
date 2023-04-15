from flask import Flask, render_template, redirect, request


app = Flask(__name__)

astro_form_d = dict()


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


@app.route("/astronaut_selection", methods=['POST', 'GET'])
def astronaut_form():
    if request.method == 'GET':
        return render_template("astronaut_form.html")
    elif request.method == 'POST':
        astro_form_d["surname"] = request.form.get("surname")
        astro_form_d["name"] = request.form.get("name")
        astro_form_d["email"] = request.form.get("email")
        astro_form_d["education"] = request.form.get("education")
        astro_form_d["job"] = request.form.get("job")
        astro_form_d["sex"] = request.form.get("sex")
        astro_form_d["about"] = request.form.get("about")
        astro_form_d["accept"] = request.form.get("accept")
        return redirect('/auto_answer')


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    astro_form_d["title"] = "Ответ"
    return render_template("auto_answer.html", **astro_form_d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
