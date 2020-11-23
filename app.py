import sqlite3
from flask import Flask, render_template, request, redirect, g
app = Flask(__name__)

# Path to sqlite3 database
DATABASE = 'data/test_database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cur = get_db().cursor() #  Get the database cursor (this allows us to issue query statements)
    select_all = cur.execute('SELECT * from users;')
    rv = select_all.fetchall()
    print('\n')
    print(rv)
    print('\n')
    
    return render_template('index.html', all_rows=rv)

# Flask routes support GET requests by default. 
# However it must be declared if the methods argument is provided.
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("sign_up.html", feedback=feedback)

        return redirect(request.url)

    return render_template("sign_up.html")


app.run(debug=True)