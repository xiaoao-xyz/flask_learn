from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="template")
bootstrap = Bootstrap(app)


@app.route('/')
def index():

    # return '<h1>Hello, World!</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return '<h1>Welcome, %s</h1>' % name
    return render_template('user.html', name = name)

@app.route('/ua')
def get_ua():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your User Agent:</h1>\n<strong>%s</strong>' % user_agent


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)