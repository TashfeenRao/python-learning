from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello world</h1>"

@app.route('/information')

def info():
    return "<h1>Some cute baby is on my town</h1>"


@app.route('/somename/<name>')

def dynamic_name(name):
    return "<h1>This is my new name {}</h1>".format(name)

@app.route('/puppy/<name>')

def puppy_name(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'ifull'
    else:
        pupname = name + 'y'
    return "<h1>your puppy {} latine name is {}</h1>".format(name,pupname)
if __name__ == '__main__':
    app.run(debug=True)