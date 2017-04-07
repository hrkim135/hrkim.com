# main.py

from bottle import *

@route("/")
def index():
    return template("index")

@route("/todo")
def todo():
    return template("todo")

run(host="localhost", port=8080)
