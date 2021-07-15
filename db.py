import sqlite3
from flask import Flask
con = sqlite3.connect("main.db")
cur = con.cursor()
#테이블 생성
#cur.execute("CREATE TABLE user (user_id int, username varchar(50), password varchar(50));")

#데이터 생성
# cur.execute("INSERT INTO user(user_id, username, password) VALUES(1, 'siyeon','pw');")
# con.commit()

#데이터 삭제
cur.execute("DELETE FROM user WHERE user_id=1;")
con.commit()

app =None

@app.route("/hello")
def hello():
    cur.execute("sql")
    return ""