# main.py

from bottle import *

@route("/")
def index():
    return template("index")

run(host="localhost", port=8080)
