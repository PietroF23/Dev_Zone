from download_db import read_db, update_db, read_localdb
update_db()
db = read_db()
localdb = read_localdb()
print(db)
print(type(db))
try:
    for key, val in db.items():
        for v, num in val.items():
            print(v)
            print(db['gelati'][f'{v}'])
            #print(key, "-->", v, ":", num, val)
    print(db['gelati'])
except KeyError:
    print("Errore chiave")


for key, val in localdb.items():
    print("Gusto numero: ", key, " : ", val)
    xval = int(val)
print(localdb)
