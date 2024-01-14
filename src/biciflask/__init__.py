from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/stop')
def stop():
    return render_template('stop.html')

if __name__ == '__main__':
    app.run(debug=True)
