# Kolbeinn Ingólfsson og Águst örn Eiðsson
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
listivorur = []
kulVara = 0
teljari = 0

asd = []
print(numrows)
for x in range(numrows):
    row = cursor.fetchone()
    asd.append(row)
    if row:
        teljari += 1
        vorur = {}
        vorur["voruid"] = row[0]
        vorur["name"] = row[1]
        vorur["verd"] = row[2]
        listivorur.append(vorur)





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
def karfa():
    session = request.environ.get('beaker.session')
    karfa = []
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
                print(asd[i][2])

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
            print(asd[x][0])
            session.save()
            return redirect('/karfa')


@route('/karfa/eyda')
def eyda_ur_korfu():
    session = request.environ.get('beaker.session')
    session.delete()
    global verdK
    verdK = 0
    return redirect('/karfa')

#run(host='0.0.0.0', port="argv[1]")
run(host='localhost', port=8080, app=app)
