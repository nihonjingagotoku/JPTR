from flask import Flask
import os


def create_and_fill_db(db_name="dictionary_app_database.db", data_name="dictionary_data.txt"):
    import sqlite3
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE DICTIONARY(WID INTEGER PRIMARY KEY AUTOINCREMENT,
    WTYPE TEXT, JPWORD TEXT, KANJI TEXT, ROMAJI TEXT, TRMEANING TEXT)""")
    
    content = open(data_name, "r").readlines()
    for counter, item in enumerate(content):
        if item.startswith("//") == True:
            continue
        else:
            splitted = item.split("|")
            try:
                cur.execute("INSERT INTO DICTIONARY(WTYPE, JPWORD, KANJI, ROMAJI, TRMEANING) VALUES (?,?,?,?,?)", 
                    (splitted[0], splitted[1], splitted[2], splitted[3], splitted[4]) )
            except Exception as e:
                item = item.strip()
                print(e, f"l:{counter+1} \'{item}\'")
    con.commit()
    con.close()
    
def create_app():
    app = Flask(__name__) 
    osenv = os.environ
    if "DICTIONARY_APP_DATABASE" in osenv and "DICTIONARY_APP_DATA" not in osenv:
        app.config["DATABASE"] = osenv["DICTIONARY_APP_DATABASE"]
    elif "DICTIONARY_APP_DATABASE" in osenv and "DICTIONARY_APP_DATA" in osenv:
        app.config["DATABASE"] = osenv["DICTIONARY_APP_DATABASE"]
        create_and_fill_db(osenv["DICTIONARY_APP_DATABASE"], osenv["DICTIONARY_APP_DATA"])
    else:
        if "dictionary_app_database.db" not in os.listdir():
            create_and_fill_db()
            print("[+] Database created!")
        app.config["DATABASE"] = "dictionary_app_database.db"

    import db
    db.init_app(app)
    
    from routes import blueprint
    app.register_blueprint(blueprint)

    return app

