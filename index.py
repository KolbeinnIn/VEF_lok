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
        print(row)
        teljari += 1
        vorur = {}
        vorur["voruid"] = row[0]
        vorur["name"] = row[1]
        vorur["verd"] = row[2]
        listivorur.append(vorur)


print(asd[2][0])



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
    for x in range(numrows+1):
        if session.get(x):
            vara = session.get(x)
            karfa.append(vara)

    return template('karfa.tpl', karfa=karfa)

@route('/karfa/baeta/<id:int>')
def baeta_i_korfu(id):
    for x in range(len(asd)):
        if id == x:
            session = request.environ.get('beaker.session')
            session[id] = 'Vara '+str(id)
            session.save()
            return redirect('/karfa')

        elif id in asd[x]:
            session = request.environ.get('beaker.session')
            session[asd[x][0]] = 'Vara ' + str(asd[x][x]) + "asdasd"
            print(asd[x-1][0])
            session.save()
            return redirect('/karfa')



@route('/karfa/eyda')
def eyda_ur_korfu():
    session = request.environ.get('beaker.session')
    session.delete()
    return redirect('/karfa')

#run(host='0.0.0.0', port="argv[1]")
run(host='localhost', port=8080, app=app)
