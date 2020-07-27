
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__, template_folder="template")

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    "mysql+pymysql://root:074057@localhost:3306/test?charset=UTF8"
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

class NameForm(FlaskForm):
    
    #第一个参数对应form.name.label
    #name属性的获取forms.name()
    #name属性的设置
    name = StringField('What is your name?', validators=[Required()])

    submit = SubmitField('Submit')


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    
    if form.validate_on_submit():
        old_name = session.get('name')
        # flash('HiJack!')
        if old_name is not None and old_name != form.name.data:
            flash('Look like you have changed your name!')
        session['name'] = form.name.data#对于不存在的键会自动返回None
        return redirect(url_for('index'))
        # name = form.name.data
        # form.name.data = '啊'
    # return '<h1>Hello, World!</h1>'

    print(session.get('name'))
    return render_template('index.html',
                            form = form,
                            name = session.get('name'),
                            current_time=datetime.utcnow())

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

@app.route('/table', methods= ['GET', 'POST'])
def fill_form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('table.html', forms=form, name=name)

with app.test_request_context():
    print(url_for('get_ua', _external=True, lol=3))
    from pprint import pprint

    # print(app.config)

if __name__ == '__main__':
    app.run(debug=True)
    manager.run()