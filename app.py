from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Flask routes support GET requests by default. 
# However it must be declared if the methods argument is provided.
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        # Without capturing form data as 'req' variable

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        print('\n', username, email, password)

        # Alternatively

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        print('\n', username, email, password, '\n')

        return redirect(request.url)

    return render_template("sign_up.html")


app.run(debug=True)