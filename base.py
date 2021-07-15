from flask import Flask, render_template
import pygame

app = Flask(__name__)

x = 3

print(x)
print(x)
print(x)


@app.route('/')
def index():
    try:
        print(x)
    except:
        pass
    print(x)
    logged_in = True
    print(x)
    numbers_list = [1, 2, 3, 4, 5, 6, 7]
    puppy_list = ['jugnu', 'majno', 'lalla']
    return render_template('basic.html', numbers_list=numbers_list, puppy_list=puppy_list, logged_in=logged_in)


# def index():
#     name = 'tashfeen'
#     letters = list(name)
#     dic = {"jugnu": "puppy"}
#     return render_template('basic.html',name=name, letters=letters, dic = dic)


@app.route('/information')
def info():
    return "<h1>Some cute baby is on my town</h1>"


@app.route('/somename/<name>')
def dynamic_name(name):
    return "<h1>This is my new name {}</h1>".format(name)


@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/puppy/<name>')
def puppy_name(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'ifull'
    else:
        pupname = name + 'y'
    return render_template("puppy.html", pupname=pupname)


if __name__ == '__main__':
    app.run(debug=True)
