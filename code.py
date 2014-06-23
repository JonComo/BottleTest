from bottle import route, run, template
import threading
import time

from PIL import Image

class App():

    counter = 0

    image = Image.new('RGB', (100, 100), "black")  # create a new black image
    image.save('output.png')

    def __init__(self):
        self.t1 = threading.Thread(target=self.loop)
        self.t1.start()

    def loop(self):
        while True:
            self.counter += 1
            time.sleep(1)

app = App()

@route('/')
def index():
    return template('index', time=app.counter)

#run(host='localhost', port=8080)
run(host='0.0.0.0', port=8080)