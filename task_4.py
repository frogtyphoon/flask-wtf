from flask import Flask, url_for, request, render_template


app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    form = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'speciality': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template('auto_answer.html', form=form, title=form['title'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')