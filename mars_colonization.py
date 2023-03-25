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
    image = f'''<img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
    return f"<h1>Жди нас, Марс!</h1></br>{image}</br>Вот она какая, красная планета"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
