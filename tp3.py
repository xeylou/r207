def first_function():
    import sqlite3 as sql
    con = sql.connect("bdd_cours.sqlite")
    cur = con.cursor()

    cur.execute("select * from Cours")

    res = cur.fetchall()

    # catching results and read each lines in row
    # for row in res:
    #     (cours,prof) = tuple(row)
    #     print("- "+cours+" -> "+prof)
    
    print("fin.")
    con.close()