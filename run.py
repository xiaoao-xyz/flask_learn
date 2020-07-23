from flask import Flask, render_template


app = Flask(__name__, template_folder="template")


@app.route('/')
def index():

    # return '<h1>Hello, World!</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return '<h1>Welcome, %s</h1>' % name
    return render_template('user.html', name = name)




if __name__ == '__main__':
    app.run(debug=True)