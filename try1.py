from flask import Flask, render_template
from flask import Flask, request
import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    database='chat_app'
)

cursor = conn.cursor()

app = Flask(__name__)

title = "about"
title2 = "home"
title3 = "login"
title4 = "signup"
name = "kavishka"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title2 = title2, name = name)

@app.route("/about")
def about():
    return render_template('about.html', title = title, name = name)

@app.route("/login")
def login():
    return render_template('login.html', title3 = title3, name = name)

@app.route("/signup")
def signup():
    return render_template('signin.html', title4 = title4, name = name)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # Your code here
    return "Received: " + projectpath

app.run(host="0.0.0.0", port=5505)
