from PIL import Image
from flask import Flask, render_template
from flask.wrappers import Response

import numpy as np

import io

ROW, COLUMN = 450, 800

app = Flask(__name__)


def generate_images():
    pixel_array = list()
    for i in range(0, ROW * COLUMN):
        pixel_array.append(0)

    while True:
        pixel_array[0] += 1
        if pixel_array[0] > 255:
            for i in range(0, len(pixel_array)):
                if pixel_array[i] > 255:
                    pixel_array[i] -= 255
                    pixel_array[i + 1] += 1

        if pixel_array[-1] > 255:
            break

        pa_counter = 0
        img_matrix = np.empty((ROW, COLUMN))

        for row in range(0, ROW):
            for column in range(0, COLUMN):
                img_matrix[row][column] = pixel_array[pa_counter]
                pa_counter += 1

        img = Image.fromarray(img_matrix, "L")

        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        img_bytes = buf.getvalue()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video-feed')
def video_feed():
    return Response(generate_images(), mimetype='multipart/x-mixed-replace;boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
