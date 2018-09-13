import sqlite3

def select_task_name(pid):
    cur.execute("select name from peopleid where id = ?",(pid,))
    row = cur.fetchone()
    return row[0]

def select_task_id(pname):
    cur.execute("select id from peopleid where name = ?",(pname,))
    row = cur.fetchone()
    return row[0]

def insert_value(pid,pname):
    cur.execute("insert into peopleid values (?,?)",(pid,pname))
    con.commit()

db = "recognizer/facedet.db"
global con,cur
try:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists peopleid(id INTEGER PRIMARY KEY NOT NULL,name VARCHAR(20) NOT NULL);")
except Error as e:
    print(e)