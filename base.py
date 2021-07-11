from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello world</h1>"
    
@app.route('/information')

def info():
    return "<h1>Some cute baby is on my town</h1>"

if __name__ == '__main__':
    app.run(debug=True)