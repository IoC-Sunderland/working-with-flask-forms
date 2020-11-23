import sqlite3
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test_database.db'
db = SQLAlchemy(app)

# This defines your database table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

    # Define __repr__ that will be called when querying e.g. 'Users.query.all()'
    def __repr__(self):
        obj_repr = f'ID: {self.id},' \
                   f'Username: {self.username},' \
                   f'Email: {self.email},' \
                   f'Password: {self.password}' \

        return obj_repr


@app.route('/')
def index():
    # Display all records in db
    all_users = Users.query.all()
    return render_template('index.html', all_users=all_users)


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

        new_user = Users(username=req['username'],
                         email=req['email'],
                        password=req['password'])

        print(new_user)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/')

    return render_template("sign_up.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)