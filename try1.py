from flask import Flask, render_template
from flask import Flask, request
from flask import Flask, redirect, url_for
import mysql.connector


conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    database='chat_app'
)

cursor = conn.cursor()

app = Flask(__name__)

title = "home"
title2 = "login"
title3 = "signup"
title4 = "about"
title5 = "chat"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = title, user_name=user_name)

@app.route("/about")
def about():
    return render_template('about.html', title4 = title4)

@app.route("/login")
def login():
    return render_template('login.html', title2 = title2)

@app.route("/signup")
def signup():
    return render_template('signin.html', title3= title3)

@app.route("/chat")
def chat():
    return render_template('chatui.html', title5= title5, user_name_1=user_name_1, fname_1=fname_1, lname_1=lname_1, phone_1=phone_1)


@app.route('/checkuser', methods=['POST'])
def checkuser():
        global user_name
        user_name = request.form.get('usr_nme')
        passowrd = request.form.get('pwd')

        data = [user_name,passowrd] # ["kavishka_dulshan","aaa"]
        data1 = [user_name] # ['kavishka_dulshan']
        list1 = [] # []
        list3 = [] # []
        query = "SELECT*FROM user where user_name=" "%s"
        cursor.execute(query,data1)
        result = cursor.fetchall()
        conn.commit()

        for i in result:
            list1.append(i[1])
            list1.append(i[4])

        for i in list1:
            for j in data:
                if i==j:
                    list3.append(j)

        if data == list3:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
        
@app.route("/adduser", methods=['POST'])
def adduser():
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        user_name = request.form.get('user_name')
        passwd = request.form.get('passwd')
        confpasswd = request.form.get('confpasswd')
        phone = request.form.get('phone')
        data = [user_name,fname,lname,passwd,phone]

        if passwd == confpasswd:
            query = ("insert into user (user_name,fname,lname,pwd,phone) values (%s,%s,%s,%s,%s)")
            cursor.execute(query,data)
            conn.commit()
            return redirect('login')
        else:
            return "Something went wrong" 
        
@app.route("/finduser", methods=['POST'])
def finduser():
     find = request.form.get('username')
     data = [find]
     
     query = "select * from user where user_name =" "%s" 
     cursor.execute(query,data)
     result = cursor.fetchall()
     conn.commit()
    
     global user_name_1,fname_1,lname_1,phone_1
     user_name_1 = result[0][1]
     fname_1 = result[0][2]
     lname_1 = result[0][3]
     phone_1 = result[0][5]

     return redirect(url_for('chat'))
        

app.run(host="0.0.0.0", port=5505, debug=True)
