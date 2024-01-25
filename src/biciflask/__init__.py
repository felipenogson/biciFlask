from flask import Flask
from flask_jwt_extended import JWTManager 

app = Flask(__name__) 
app.config['JWT_SECRET_KEY'] = 'esto es super secreto paps, obvio hay que cambiarlo!!!'
jwt = JWTManager(app)

from biciflask import routes

if __name__ == '__main__':
    app.run(debug=True)
