import sqlite3
def connect():
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST book(id INTEGER PRIMARY KEY,reminder text)")
    conn.commit()
    conn.close()

def insert(rid,reminder):
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO rm VALUES(NULL,?)"(reminder))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM rm")
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(id):
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("DELETE from rm WHERE id=?,(id,)")
    rows=cur.fetchall()
    conn.close()
    return rows 
def update(id,remind):
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("UPDATE rm SET title=? WHERE id=?",(reminder)")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows 

    