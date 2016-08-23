import time
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from celery import Celery
from hashids import Hashids
from convert import convert
import shutil

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'amqp://myuser:mypassword@localhost:5672/myvhost'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

CORS(app)


@app.route('/')
def index():
    return 'hello'


@app.route('/create_video', methods=['POST'])
def create_video():
    data = request.get_json(silent=True)

    hashids = Hashids(alphabet='abcdefghijklmnopqrstuvwxyz0123456789')
    vid = hashids.encode(int(time.time()*1000000))
    filename = 'videos/{}.mp4'.format(vid)
    url = 'http://localhost:5000/videos/{}.mp4'.format(vid)

    create_async_video.delay(data, filename)

    return jsonify(url=url)


@app.route('/videos/<path:path>')
def send_vid(path):
    return send_from_directory('videos', path)


@celery.task
def create_async_video(data, filename):
    print filename
    shutil.copyfile('processing.mp4', filename)
    convert(data, outfile=filename)


if __name__ == "__main__":
    app.run()
