import os
import requests
import json

url = 'https://raw.githubusercontent.com/PietroF23/Server_0.1/main/db.json'
url2 = 'https://raw.githubusercontent.com/PietroF23/Server_0.1/main/localdb.json'

def update_db():
    print("Aggiornamento in corso!")
    try:
        os.remove("db.json")
        with open("db.json", "w") as f:
            page = requests.get(url)
            txt = page.text
            data = json.loads(txt)
            json.dump(data, f)
            print("Aggiornamento terminato!")
    except FileNotFoundError:
        with open("db.json", "w") as f:
            page = requests.get(url)
            txt = page.text
            data = json.loads(txt)
            json.dump(data, f)
            print("Aggiornamento terminato!")

def read_db():
    try:
        with open("./db.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        update_db()

    return data

def update_localdb():
    with open("./localdb.json", "w") as f:
        page = requests.get(url2)
        txt = page.text
        data = json.loads(txt)
        json.dump(data, f)

def read_localdb():
    try:
        with open("./localdb.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        update_localdb()
        data = read_localdb()

    return data
