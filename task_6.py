from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    astronauts = ['scot ridley', 'emma watson', 'toby']
    return render_template('distribution.html', title='По каютам!', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
