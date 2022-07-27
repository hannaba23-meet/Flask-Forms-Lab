from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/')
def login():
  return render_template('login.html')
  




@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return 'something wrong try again!'
    else:
        if username == request.form['username'] and password == request.form['password'] :
            return render_template('home.html')


@app.route('/home', methods=['GET', 'POST'])
def hello():
    return render_template(
        'home.html', y = facebook_friends)

@app.route('/friend_exists/<string:name>')
def fe(name):
    is_friend = name in facebook_friends
    return render_template('friend_exists.html', n = is_friend)
    
if __name__ == "__main__":
    app.run(debug=True)
