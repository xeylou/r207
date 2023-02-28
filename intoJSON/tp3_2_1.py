import json, sqlite3

con = sqlite3.connect("tp3_2")
cur = con.cursor()

cur.execute("select * from cours")
res = cur.fetchall()

toJSON=[]
for line in res:
    tmp=[]
    tmp.append(line[0])
    tmp.append(line[1])
    toJSON.append(tmp)
print(toJSON)

# version by julien (C)
print("[")
for line in res:
    print("[")
    for elt in line:
        print(elt, ",")
    print("]")
print("]")

con.close()