from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Flask routes support GET requests by default. 
# However it must be declared if the methods argument is provided.
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        print(req)

        return redirect(request.url)

    return render_template("sign_up.html")


app.run(debug=True)