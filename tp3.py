import sqlite3 as sql

def first_function():
    con = sql.connect("bdd_4_sqlite.sql")
    cur = con.cursor()

    cur.execute("select * from cours")

    res = cur.fetchall()

    # catching results and read each lines in row
    # for row in res:
    #     (cours,prof) = tuple(row)
    #     print("- "+cours+" -> "+prof)

    print("fin.")
    con.close()

print(first_function())