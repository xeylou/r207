import sqlite3 as sql

con = sql.connect("magasin_sqlite")
cur = con.cursor()

cur.execute("select * from produit")

res = cur.fetchall()

print("fin.")
con.close()