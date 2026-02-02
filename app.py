from flask import Flask, render_template, request, flash

app= Flask(__name__) #creates class
app.secret_key ="basucbaa890998"

@app.route("/hello")
def index():
    flash("What's your name")
    return render_template("index.html")

@app.route("/greet" , methods= ["POST", "GET"])
def greet():
    flash("Hi"+ str(request.form['name_input'])+ ",greate to see yiu")
    return render_template("index.html")
     

