from bottle import *
from sys import argv

@route("/")
def index():
    return "Flott síða"


run(host="0.0.0.0", port=argv[1])
