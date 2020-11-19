from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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