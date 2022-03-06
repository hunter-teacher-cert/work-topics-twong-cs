from flask import render_template, flash, redirect
from flask import Flask, request,session 

import random

app = Flask(__name__)
app.secret_key="something"

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route("/login",methods=['GET','POST'])
def login():
  if request.method=="GET":
    return render_template("login.html")
  else:
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if name != "tiffany":
      error = "No account with that username found."
      name = ""
      pw = ""
    if name == "tiffany" and pw != "12345":
        error = "Incorrect password."
        pw = ""
    if name == "tiffany" and pw == "12345":
      error = ""
  return render_template("login.html",error=error, name=name)

@app.route("/welcome")
def welcome():
  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1
  return render_template("welcome.html",count = session['count'])


app.run(host="0.0.0.0",port=5000,debug=True)