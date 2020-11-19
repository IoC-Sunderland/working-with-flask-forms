from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Flask routes support GET requests by default. 
# However it must be declared if the methods argument is provided.
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        username = req.get("username")
        email = req["email"]
        password = request.form["password"]

        description = (f"\nUsername is: {username}\n"
                       f"Email is: {email}\n"
                       f"Password is: {password}\n")
        
        print(description)

        return redirect(request.url)

    return render_template("sign_up.html")


app.run(debug=True)