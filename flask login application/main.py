from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def about():
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")





if __name__=="__main__":
    app.run(host="0.0.0.0",port=5008)
