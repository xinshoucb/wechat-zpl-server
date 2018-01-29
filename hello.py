from flask import Flask
import handler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'zhao piao liang!'

@app.route('/infos', methods=['GET'])
def get_infos():
    return handler.get_events()

@app.route('/add', methods=['GET', 'POST'])
def add_infos():
    return handler.save_event()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1025)