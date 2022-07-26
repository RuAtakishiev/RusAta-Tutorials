from flask import Flask
from flask import render_template
from flask import request
from flask import flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Justkey'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "О сайте", "url": "about"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='О сайте', menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено',  category='success')
        else:
            flash('Ошибка отправки',  category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)