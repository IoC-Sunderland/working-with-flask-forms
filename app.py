from flask import Flask, render_template
app = Flask(__name__)

@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")


app.run(debug=True)