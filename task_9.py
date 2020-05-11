from flask import Flask, url_for, request, render_template
from PIL import Image
from io import BytesIO
import json

app = Flask(__name__)


@app.route('/member')
def member():
    with open("templates/members.json", "rt", encoding="utf8") as f:
        members = json.loads(f.read())
        return render_template('member.html', title='Личная карточка', members=members,
                               male_boy_url=url_for('static', filename='img/male_boy.jpg'),
                               male_man_url=url_for('static', filename='img/male_man.jpg'),
                               female_girl_url=url_for('static', filename='img/female_girl.jpg'),
                               female_woman_url=url_for('static', filename='img/female_woman.jpg')
                               )


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
