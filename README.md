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
