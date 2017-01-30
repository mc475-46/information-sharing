from bottle import route, run, template, static_file, url, request


@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root="./static")


@route('/')
def home():
    return template('template/home.html')


@route('/person')
def person():
    return template('template/person.html')


@route('/person/<search_from>')
def search_person(search_from):
    if search_from == "department":
        return template('template/person/department.html')
    elif search_from == "project":
        return template('template/person/project.html')
    elif search_from == "club":
        return template('template/person/club.html')
    elif search_from == "ryugaku":
        return template('template/person/ryugaku.html')
    elif search_from == "skilltree":
        return template('template/person/skilltree.html')
    elif search_from == "1":
        return template('template/person/taro.html')
    else:
        return template('template/not_implemented.html')


@route('/person/department/class')
def search_person_from_class():
    return template('template/person/class.html')


@route('/person/department/list')
def search_person_from_list():
    return template('template/person/list.html')


@route('/search')
def search():
    search_string = request.query.search
    return template('template/search.html', search_string=search_string)


@route('/not_implemented')
def not_implemented():
    return template('template/not_implemented.html')


from os import environ
if environ.get("IS_HEROKU"):
    run(server='gunicorn', host='0.0.0.0', port=int(environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True, reloader=True)