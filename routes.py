from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for, session
import db

blueprint = Blueprint('jptrdict', __name__, template_folder='templates')

@blueprint.route("/")
def index():
    return redirect(url_for("jptrdict.sozluk"))

@blueprint.route("/sozluk")
def sozluk():
    dop = db.get_db()
    search = request.args.get('search')
    if search=='' or search==None:
        search=None
        all_words = request.args.get('all')
        if all_words == "1":
            lazy_db = dop.execute("SELECT * FROM DICTIONARY").fetchall()
        else:        
            lazy_db = dop.execute("SELECT * FROM DICTIONARY ORDER BY RANDOM() LIMIT 9").fetchall()
    else:
        search_opt = request.args.get('search_opt')

        if search_opt == 'Türkçe' or search_opt == 'Japonca' or search_opt == 'Romaji':
            if (search_opt == "Türkçe"):
                lazy_db = dop.execute(f"SELECT * FROM DICTIONARY where trmeaning like '{search}%'").fetchall()
            elif (search_opt == "Japonca"):
                lazy_db = dop.execute(f"SELECT * FROM DICTIONARY where jpword like '{search}%'").fetchall()
                if len(lazy_db) == 0:
                    lazy_db = dop.execute(f"SELECT * FROM DICTIONARY where kanji like '{search}%'").fetchall()  
            elif (search_opt == "Romaji"):
                lazy_db= dop.execute(f"SELECT * FROM DICTIONARY where romaji like '{search}%'").fetchall()
        else:
            lazy_db=None

    return render_template("index.html",search=search, db_results=lazy_db)

@blueprint.route("/sozluk/addword", methods=['GET', 'POST'])
def sozluk_addword():
    if request.method == 'POST':
        try:
            w=request.form['jpword']
            t=request.form['wtype']
            k=request.form['kanji']
            r=request.form['romaji']
            tr=request.form['trmeaning']
        except:
            return render_template("addword.html", fail=True)
            
        wlen = len(w)
        tlen = len(t)
        klen = len(k)
        rlen = len(r)
        trlen = len(tr)
        
        cond = wlen>0 and tlen>0 and klen>0 and rlen>0 and trlen>0
        
        if (cond == False):
            return render_template("addword.html", fail=True)
 
        handle = db.get_db()
        handle.execute("INSERT INTO DICTIONARY (wtype, jpword, kanji, romaji, trmeaning) VALUES (?,?,?,?,?)", (t,w,k,r,tr))
        handle.commit()
        return redirect(url_for("jptrdict.sozluk_addword"))
    else:
        return render_template("addword.html")

@blueprint.route("/sozluk/statistics")
def sozluk_statistics():
    dop = db.get_db()
    rows = dop.execute("SELECT COUNT(*) from DICTIONARY").fetchone()[0]
    arg_all = request.args.get('all')
    if arg_all == "1":
        all_words = dop.execute("SELECT * FROM DICTIONARY")
    else:
        all_words = None
    
    return render_template("statistics.html", RowCount=rows, ListAll=all_words)
