from bottle import *

@route("/")
def index():
    return "Flott síða"


run(host="0.0.0.0")