def first_function():
    import sqlite3 as sql
    con = sql.connect("bdd_cours.sqlite")
    cur = con.cursor()
    cur.execute("select distinct NomCours,NomProf from Cours,Suit where (Suit.NumCours = Cours.NumCours)")
    res = cur.fetchall()
    for row in res:
    (cours,prof) = tuple(row)
    print("- "+cours+" -> "+prof)
    print("fin.")
    con.close()