from flask import Flask, jsonify, render_template
import time

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():

    return render_template('start.html')

@app.route('/startTimer', methods=['POST'])
def startTimer():
    startTime = time.time_ns() / 1000000
    return jsonify(startTime)

@app.route('/stop')
def stop():
    return render_template('stop.html')

if __name__ == '__main__':
    app.run(debug=True)
