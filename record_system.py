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


def View_one(id=None, name=None):
    conn = con()
    cur = conn.cursor()

    if id:
        cur.execute("SELECT * FROM july WHERE id = ?", (id,))
        row = cur.fetchone()
        print(row)

    elif name:
        cur.execute("SELECT * FROM july WHERE name = ?", (name,))
        row = cur.fetchone()
        print(row)

    else:
        print("Enter either id or name.")

    conn.close()


    
def View_all():
    conn = con()
    cur = conn.cursor()

    cur.execute("SELECT * FROM july")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()
    


   
def Delete(id=None, name=None):
    conn = con()
    cur = conn.cursor()

    if id:
        cur.execute("DELETE FROM july WHERE id = ?", (id,))
    elif name:
        cur.execute("DELETE FROM july WHERE name = ?", (name,))
    else:
        print("Enter either id or name.")
        conn.close()
        return

    conn.commit()

    if cur.rowcount > 0:
        print(f"{cur.rowcount} record(s) deleted successfully.")
    else:
        print("No matching record found.")

    conn.close()



 
def update(id, name=None, age=None, branch=None, marks=None):
    conn = con()
    cur = conn.cursor()

    cur.execute("SELECT * FROM july WHERE id = ?", (id,))
    row = cur.fetchone()

    if not row:
        print("Person not found.")
        conn.close()
        return

    #keep the old value is new vaues are not given
    new_name = name if name is not None else row[1]
    new_age = age if age is not None else row[2]
    new_branch = branch if branch is not None else row[3]
    new_marks = marks if marks is not None else row[4]

  

 

