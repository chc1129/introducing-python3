from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='.')
