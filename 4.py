from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def fp():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "<p>Человечество вырастает из детства. </p>" \
           "<p>Человечеству мала одна планета. </p>" \
           "<p>Мы сделаем обитаемыми безжизненные пока планеты. </p>" \
           "<p>И начнем с Марса!</p>" \
           "<p>Присоединяйся!</p>"


@app.route('/image_mars')
def image_mars():
    return "<title>Привет, Марс!</title>" \
           "<h1>Жди нас, Марс!</h1>" \
           """<img src="https://i.pinimg.com/originals/9a/bb/7e/9abb7ea3569ae7fffbef6ac93842e9de.gif">
                <p>Вот она какая, красная планета.</p>"""


@app.route('/promotion_image')
def promotion_image():
    return render_template("4.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
