import sqlite3
base= "july26"

#DATABASE =>>>

def con():
    return sqlite3.connect(base)

def Table():
    conn = con()
    cur = conn.cursor()
    
    cur.execute("""
                CREATE TABEL IF NOT EXISTS july(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR,
                    age INTEGER,
                    branch VARCHAR,
                    marks INTEGER
                )""")
    conn.commit()
    conn.close()
    
def Add(name , age , branch , marks):
    conn = con()
    cur = conn.cursor()
    
    cur.execute("""INSERT INTO july(name , age , branch , marks) VALUES (?,?,?,?)"""
                ( name , age , branch , marks)) 
    
    conn.commit()
    conn.close()
