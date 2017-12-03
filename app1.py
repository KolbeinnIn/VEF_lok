# Kolbeinn Ingólfsson og Águst Örn Eiðsson
# 29.11.2017
# Lokaverkefni - VEF

from bottle import *
from pymysql import *
from beaker.middleware import SessionMiddleware


db = Connect(host="tsuts.tskoli.is", user="0908002640", password="mypassword", db="0908002640_vefLok")
cursor = db.cursor()
cursor.execute("select * from vorur")
numrows = int(cursor.rowcount)
vorur = {}
karfa = []

asd = []
for x in range(numrows):
    row = cursor.fetchone()
    asd.append(row)


@error(404)
def index():
    return "villa"
    #villa = "Villa"
    #return template("villa", villa=villa)

@error(500)
def index():
    villa = "Villa"
    return template("villa", villa=villa)

@route('/static/<filepath>')
def static(filepath):
    return static_file(filepath, root='./static')

@route('/static/css/<filepath>')
def static(filepath):
    return static_file(filepath, root='./static/css')

sess = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), sess)




@route('/')
def index():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()
    return template('index.tpl', asd=asd, teljari=s['test'])

@route('/karfa')
def karfan():
    karfa = []
    session = request.environ.get('beaker.session')
    verdK = 0
    for x in range(numrows+1):
        if session.get(x):
            vara = session.get(x)
            karfa.append(vara)
            print(karfa)
    for x in karfa:
        for i in range(len(asd)):
            if x == asd[i][1]:
                verdK += asd[i][2]

    return template('karfa.tpl', karfa=karfa, verd=verdK)

@route('/karfa/baeta/<id:int>')
def baeta_i_korfu(id):
    for x in range(len(asd)):
        """if id == x:
            print("asd")
            session = request.environ.get('beaker.session')
            session[id] = 'Vara '+str(id)
            session.save()
            return redirect('/karfa')"""

        if id in asd[x]:
            session = request.environ.get('beaker.session')
            session[x] = asd[x][1]
            session.save()
            return redirect('/karfa')


@route('/karfa/eyda')
def eyda_ur_korfu():
    session = request.environ.get('beaker.session')
    session.delete()
    global verdK
    verdK = 0
    return redirect('/karfa')

@route("/karfa/<name>")
def index(name):
    for x in asd:
        if name in karfa:
            if name == x[1]:
                print(x)
                global u
                u = str(x[3]).replace("\r", "").split("\n")
                global a
                a = x[1]
                break
            else:
                return redirect("/")
        else:
            return redirect("/")

    return template("uppl", a=a, u=u)

run(host='0.0.0.0', port="argv[1]", app=app)
