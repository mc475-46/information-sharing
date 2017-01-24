from bottle import route, run, template, static_file, url


@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root="./static")


@route('/')
def home():
    return template('template/home.html', url=url)


@route('/person')
def person():
    return template('template/person.html', url=url)


@route('/search')
def search():
    return template('template/not_implemented.html', url=url)

from os import environ
if environ.get("IS_HEROKU"):
    run(server='gunicorn', host='0.0.0.0', port=int(environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True, reloader=True)