from flask import render_template, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import math, time
from biciflask import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/startTimer', methods=['POST'])
def startTimer():
    startTime = math.floor(time.time_ns()/1000000)
    print(f'funcion startTimer()StartTime: {startTime}')
    access_token = create_access_token(identity=str(startTime))
    return jsonify({'token': access_token, 'startTime': startTime })

@app.route('/stopTimer', methods=['POST'])
@jwt_required()
def stopTimer():
    data = request.get_json()
    current_user = get_jwt_identity()
    print(f'Current_user: {current_user}')
    print(f'Data: {data["startTime"]}')
    return jsonify('ok')

@app.route('/stop')
def stop():
    return render_template('stop.html')
