import sqlite3

base = "july26.db"


# DATABASE CONNECTION
def con():
    return sqlite3.connect(base)


# CREATE TABLE
def Table():
    conn = con()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS july(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            branch TEXT,
            marks INTEGER
        )
    """)

    conn.commit()
    conn.close()


# ADD RECORD
def Add(name, age, branch, marks):
    conn = con()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO july(name, age, branch, marks) VALUES (?, ?, ?, ?)",
        (name, age, branch, marks)
    )

    conn.commit()
    conn.close()


# VIEW ONE RECORD
def View_one(id=None, name=None):
    conn = con()
    cur = conn.cursor()

    if id is not None:
        cur.execute("SELECT * FROM july WHERE id = ?", (id,))
        row = cur.fetchone()
        print(row)

    elif name is not None:
        cur.execute("SELECT * FROM july WHERE name = ?", (name,))
        row = cur.fetchone()
        print(row)

    else:
        print("Enter either ID or Name.")

    conn.close()


# VIEW ALL RECORDS
def View_all():
    conn = con()
    cur = conn.cursor()

    cur.execute("SELECT * FROM july")
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")

    conn.close()


# DELETE RECORD
def Delete(id=None, name=None):
    conn = con()
    cur = conn.cursor()

    if id is not None:
        cur.execute("DELETE FROM july WHERE id = ?", (id,))

    elif name is not None:
        cur.execute("DELETE FROM july WHERE name = ?", (name,))

    else:
        print("Enter either ID or Name.")
        conn.close()
        return

    conn.commit()

    if cur.rowcount > 0:
        print(f"{cur.rowcount} record(s) deleted successfully.")
    else:
        print("No matching record found.")

    conn.close()


# UPDATE RECORD
def update(id, name=None, age=None, branch=None, marks=None):
    conn = con()
    cur = conn.cursor()

    cur.execute("SELECT * FROM july WHERE id = ?", (id,))
    row = cur.fetchone()

    if not row:
        print("Record not found.")
        conn.close()
        return

    new_name = name if name is not None else row[1]
    new_age = age if age is not None else row[2] 
    new_branch = branch if branch is not None else row[3]
    new_marks = marks if marks is not None else row[4]

    cur.execute("""
        UPDATE july
        SET
            name = ?,
            age = ?,
            branch = ?,
            marks = ?
        WHERE id = ?
    """, (new_name, new_age, new_branch, new_marks, id))

    conn.commit()
    print("Updated successfully.")
    conn.close()


# CREATE TABLE BEFORE STARTING
Table()


# MAIN MENU
while True:

    print("\n===== DATABASE MENU =====")
    print("1. Add Record")
    print("2. View One Record")
    print("3. View All Records")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")

    ch = input("Enter your choice: ")

    # ADD
    if ch == "1":
        try:
            name = input("Enter Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            age = int(input("Enter Age: "))
            branch = input("Enter Branch: ").strip()
            marks = int(input("Enter Marks: "))

            Add(name, age, branch, marks)

            print("Record Added Successfully!")

        except ValueError:
            print("Age and Marks must be numbers.")

    # VIEW ONE
    elif ch == "2":

        search = input("Search by (1) ID or (2) Name: ")

        if search == "1":
            try:
                id = int(input("Enter ID: "))
                View_one(id=id)
            except ValueError:
                print("ID must be a number.")

        elif search == "2":
            name = input("Enter Name: ")
            View_one(name=name)

        else:
            print("Invalid choice.")

    # VIEW ALL
    elif ch == "3":
        View_all()

    # UPDATE
    elif ch == "4":

        try:
            id = int(input("Enter ID to update: "))

            print("Leave blank if you don't want to change a value.")

            name = input("New Name: ").strip()
            age = input("New Age: ").strip()
            branch = input("New Branch: ").strip()
            marks = input("New Marks: ").strip()

            update(
                id,
                name if name else None,
                int(age) if age else None,
                branch if branch else None,
                int(marks) if marks else None
            )

        except ValueError:
            print("Age, Marks, and ID must be numbers.")

    # DELETE
    elif ch == "5":

        search = input("Delete by (1) ID or (2) Name: ")

        if search == "1":
            try:
                id = int(input("Enter ID: "))
                Delete(id=id)
            except ValueError:
                print("ID must be a number.")

        elif search == "2":
            name = input("Enter Name: ")
            Delete(name=name)

        else:
            print("Invalid choice.")

    # EXIT
    elif ch == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please select between 1 and 6.")
