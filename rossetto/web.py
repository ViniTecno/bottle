from bottle import route, run, template
from pack.bib import metros_para_centimetros

@route('/hello/<name>')
def index(name):
    name = 'bbbb'
    return template('<b>Hello {{name}}</b>!', name=name)

@route("/ex1/<metros:float>")
def route_ex1(metros):
        cm = metros_para_centimetros(metros)
        return template('{{cm}}', cm=cm)


run(host='localhost', port=8081)