import mysql.connector


conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    database='chat_app'
)

cursor = conn.cursor()


'''list2 = ['kavishka_dulshan','aaa',42424]
data = [list2[0]]
list1 = []
list3 = []
query = 'select*from user where user_name=' '%s'
cursor.execute(query,data)
result = cursor.fetchall()
conn.commit()
print(result)

for i in result:
    list1.append(i[1])
    list1.append(i[4])
    print(list1)

for i in list1:
    for j in list2:
        if i==j:
            list3.append(j)
            print(list3)'''
            


'''@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # Your code here
    return "Received: " + projectpath'''

data = ["kaviduls","kavi","duls","kavi2021",1234234543]
query = ("insert into user (user_name,fname,lname,pwd,phone) values (%s,%s,%s,%s,%s)")
cursor.execute(query,data)
conn.commit()
