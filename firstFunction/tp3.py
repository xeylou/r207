import sqlite3 as sql

con = sql.connect("tp3_1")
cur = con.cursor()

cur.execute("select * from cours")

res = cur.fetchall()

print("<table cellpaddin='20' border='2'>")
for ligne in res:  
    print("<tr>")
    for elt in ligne:
        print("<td>", elt, "</td>")
    print("</tr>")
print("</table>")

con.close()