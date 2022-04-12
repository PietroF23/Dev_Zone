from download_db import read_db, update_db, read_localdb
import json
update_db()
db = read_db()
localdb = read_localdb()

print(localdb)
print(type(localdb))

sel = input("Inserisci il valore da modificare: ")

for key, value in localdb.items():
    if key == sel:
        localdb[key] = 1

print(localdb)


