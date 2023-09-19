from datetime import timedelta

from flask import (Flask,jsonify, redirect, render_template, request, session,
                   url_for)

import database



app = Flask(__name__)
app.config['SECRET_KEY'] = '0TO1BUgdT5HpRt2OjvvS'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)


@app.route("/", methods=["GET"])
def home():

    if request.method == "GET":
        if session.get("username") is not None:
            return redirect(url_for("dash"))
        return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login():
    #the request data will be in json format
    username = request.json["username"]
    password = request.json["password"]

    if(database.check_credentials(username, password)):
        session["username"] = username
        print(session)
        print(type(session))
        return jsonify({"success": "true"})
    else:
        return jsonify({"success": "false"})

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))



@app.route("/dashboard", methods=["GET"])
def dash():
    if session.get("username") is None:
        return redirect(url_for("home"))
   
    return render_template("dashboard.html")
    


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)