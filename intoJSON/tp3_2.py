import json, sqlite3

con = sqlite3.connect("tp3_2")
cur = con.cursor()

cur.execute("select * from cours")
res = cur.fetchall()


# print('Données en Python:',res)

# Export des données en JSON
json_string = json.dumps(res)
print('Données en JSON:',json_string)

# Export des données en JSON avec affichage "pretty"
# json_pretty_string = json.dumps(res, indent=4)
# print('Données en JSON (beautified):\n',json_pretty_string)

con.close()