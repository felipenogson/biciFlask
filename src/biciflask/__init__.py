from flask import Flask, jsonify, render_template, request

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager 
import time

app = Flask(__name__) 
# Configurando Flask por mientras, esto hay que meterlo en un objeto en su propio archivo 
app.config['JWT_SECRET_KEY'] = 'esto es super secreto paps, obvio hay que cambiarlo!!!'
jwt = JWTManager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/startTimer', methods=['POST'])
def startTimer():
    startTime = time.time_ns()/1000000
    access_token = create_access_token(identity=str(startTime))
    return jsonify(access_token)

@app.route('/stop')
def stop():
    return render_template('stop.html')

if __name__ == '__main__':
    app.run(debug=True)
