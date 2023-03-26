from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    pr = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
          "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
          "Присоединяйся!"]
    return "</br>".join(pr)


@app.route("/image_mars")
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
                            alt="здесь должна была быть картинка, но не нашлась"> <br>
                        <tr>Вот она какая, красная планета</tr>
                      </body>
                    </html>'''


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', 
                                                                            filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route("/astronaut_selection")
def astronaut_form():
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', 
                                                                            filename='css/astronaut_form.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname" 
                                        placeholder="Ваша фамилия" name="surname">
                                        <input type="name" class="form-control" id="name" 
                                        placeholder="Ваше имя" name="name"> <br>
                                        <input type="email" class="form-control" id="email" 
                                        placeholder="Ваш email" name="email"> <br>
                                        <div class="form-group">
                                            <label for="educationSelect">Ваше образование</label>
                                            <select class="form-control" id="educationSelect" name="education">
                                              <option>Начальное</option>
                                              <option>Основное общее</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее профессиональное</option>
                                              <option>Высшее</option>
                                            </select>
                                        </div> <br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" 
                                              id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" 
                                              id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div> <br>
                                        <tr>Выберите профессии</tr>
                                        <div class="form-group">
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" 
                                                id="pilot" name="job">
                                                <label class="form-check-label" 
                                                for="pilot">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" 
                                                id="builder" name="job">
                                                <label class="form-check-label" 
                                                for="builder">Строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" 
                                                id="doctor" name="job">
                                                <label class="form-check-label" 
                                                for="doctor">Врач</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" 
                                                id="eng-expl" name="job">
                                                <label class="form-check-label" 
                                                for="eng-expl">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" 
                                                id="exo" name="job">
                                                <label class="form-check-label" 
                                                for="exo">Экзобиолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" 
                                                id="meteo" name="job">
                                                <label class="form-check-label" 
                                                for="meteo">Метеоролог</label>
                                            </div>
                                        </div> <br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите участвовать?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div> <br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div> <br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" 
                                            id="acceptRules" name="accept">
                                            <label class="form-check-label" 
                                            for="acceptRules">Готовы быть добровольцем?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>{planet_name}</title>
                  </head>
                  <body>
                    <h1>Выбор: {planet_name}</h1>
                    <h2>Она находится в пределах нашей досягаемости</h2>
                    <div class="alert alert-primary" role="alert">
                      Незаселена, пока что ;)
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Лучший выбор
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Определённо точно
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Комментарий
                    </div>
                  </body>
                </html>'''


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <div class="alert alert-primary" role="alert">
                      Поздравляем, Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Составил {rating}!
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


@app.route("/carousel")
def slideshow():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                        <div id="carousel-mars" class="carousel slide" data-ride="carousel" data-interval="true">
                            <ol class="carousel-indicators">
                                <li data-target="#carousel-mars" data-slide-to="0" class="active"></li>
                                <li data-target="#carousel-mars" data-slide-to="1"></li>
                                <li data-target="#carousel-mars" data-slide-to="2"></li>
                            </ol>
                            <div class="carousel-inner" role="listbox">
                                <div class="item">
                                    <img src="{url_for('static', filename='img/mars1.jpg')}" 
                                        alt="здесь должна была быть картинка, но не нашлась">
                                </div>
                                <div class="item active">
                                    <img src="{url_for('static', filename='img/mars2.jpg')}" 
                                        alt="здесь должна была быть картинка, но не нашлась">
                                </div>
                                <div class="item">
                                    <img src="{url_for('static', filename='img/mars3.jpg')}" 
                                        alt="здесь должна была быть картинка, но не нашлась">
                                </div>
                            </div>
                            <a class="left carousel-control" href="#carousel-mars" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Предыдущий</span>
                            </a>
                            <a class="right carousel-control" href="#carousel-mars" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Следующий</span>
                            </a>
                        </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
