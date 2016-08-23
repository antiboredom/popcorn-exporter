# Popcorn Exporter
A python server that creates mp4s from on popcorn js compositions.

To install, clone the repo, create a virtual environment, and then run
```
pip install -r requirements.txt
```

After, all the python requirements are installed you may need to make two small changes to moviepy.

change line 894 in moviepy/video/VideoClip.py to:
```python
if isinstance(img, str) or isinstance(img, unicode):
```

change line 32 in moviepy/video/fx/resize.py to:
```python
arr = np.fromstring(resized_pil.tobytes(), dtype='uint8')
```

You'll also need to install imagemagick, and rabbitmq.

For imagemagick (on a mac)
```
brew install imagemagick
```

For rabbitmq, see [these instructions](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq).

Run the server with:
```
python server.js
```
or, using uswgi
```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi
```

Also make sure to start a celery worker:
```
celery -A server.celery worker
```

Finally, to test it out in popcorn, open up the javascript console and run:
```javascript
$.ajax({
  type: "POST",
  url: "http://localhost:5000/create_video",
  data: JSON.stringify(Butter.app.currentMedia.json),
  success: function(data) {
    alert('Your video is being prepared, and will be available at: ' + data.url);
  },
  contentType: "application/json",
  dataType: "json"
});
```


