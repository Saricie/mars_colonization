from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astro = StringField('ID Астронавта', validators=[DataRequired()])
    password_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('ID Капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])

    # username = StringField('Логин', validators=[DataRequired()])
    # password = PasswordField('Пароль', validators=[DataRequired()])
    # remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

astro_form_d = dict()


@app.route('/<title>')
@app.route('/index/<title>')
def main(title):
    param = dict()
    param["title"] = title
    return render_template("base.html", **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


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
