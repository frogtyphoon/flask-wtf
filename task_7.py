from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', title='Цвет каюты', sex=sex, age=age,
                           male_boy_url=url_for('static', filename='img/male_boy.jpg'),
                           male_man_url=url_for('static', filename='img/male_man.jpg'),
                           female_girl_url=url_for('static', filename='img/female_girl.jpg'),
                           female_woman_url=url_for('static', filename='img/female_woman.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
