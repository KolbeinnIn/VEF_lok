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
for x in range(numrows):
    row = cursor.fetchone()
    print(row)
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
vorurasd = [{'voruid': 1, 'name': 'Vara 1', 'price': 1000},
         {'voruid': 2, 'name': 'Vara 2', 'price': 2000},
         {'voruid': 3, 'name': 'Vara 3', 'price': 3000},
         {'voruid': 4, 'name': 'Vara 4', 'price': 4000}]
print(vorurasd)
print(listivorur)
@route('/')
def index():
    return template('test.tpl', row=row, numrows=numrows, vorur=vorur, cursor=cursor)


"""
@route('/')
def index():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()
    return template('index.tpl', vorur=vorur, teljari=s['test'])

@route('/karfa')
def karfa():
    session = request.environ.get('beaker.session')
    karfa = []

    if session.get('1'):
        vara1 = session.get('1')
        karfa.append(vara1)

    if session.get('2'):
        vara2 = session.get('2')
        karfa.append(vara2)

    if session.get('3'):
        vara3 = session.get('3')
        karfa.append(vara3)

    if session.get('4'):
        vara4 = session.get('4')
        karfa.append(vara4)

    return template('karfa.tpl', karfa=karfa)

@route('/karfa/baeta/<id:int>')
def baeta_i_korfu(id):
    if id == 1:
        session = request.environ.get('beaker.session')
        session['1'] = 'Vara 1'
        session.save()
        return redirect('/karfa')
    if id == 2:
        session = request.environ.get('beaker.session')
        session[str(id)] = vorur[id - 1]['name']
        session.save()
        return redirect('/karfa')
    if id == 3:
        session = request.environ.get('beaker.session')
        session[str(id)] = vorur[id - 1]['name']
        session.save()
        return redirect('/karfa')
    if id == 4:
        session = request.environ.get('beaker.session')
        session[str(id)] = vorur[id - 1]['name']
        session.save()
        return redirect('/karfa')
    else:
        return redirect('/')


@route('/karfa/eyda')
def eyda_ur_korfu():
    session = request.environ.get('beaker.session')
    session.delete()
    return redirect('/karfa')

"""
run(host='localhost', port=8080, debug=True, app=app)
