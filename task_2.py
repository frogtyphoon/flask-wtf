from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/training/<prof>')
def index(prof):
    return render_template('training.html', title="Тренировка", profession=prof,
                           builder_url=url_for('static', filename='img/builder.jpg'),
                           engineer_url=url_for('static', filename='img/engineer.jpg'),
                           other_url=url_for('static', filename='img/other.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
