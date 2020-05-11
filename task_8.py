from flask import Flask, url_for, request, render_template
from PIL import Image
from io import BytesIO

app = Flask(__name__)


@app.route('/gallery', methods=['POST', 'GET'])
def gallery():
    images = [url_for('static', filename='img/builder.jpg'), url_for('static', filename='img/engineer.jpg'),
              url_for('static', filename='img/other.jpg')]
    if request.method == 'GET':
        return render_template('gallery.html', title='Пейзажи Марса', images=images)
    elif request.method == 'POST':
        f = request.files['file']
        image = Image.open(BytesIO(f.read()))
        image.save('static/img/added_slide.png')
        images.append(url_for('static', filename='img/added_slide.jpg'))
        return render_template('gallery.html', title='Пейзажи Марса', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
