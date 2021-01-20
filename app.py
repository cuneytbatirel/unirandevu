from flask import Flask, render_template, url_for, flash, redirect, request, session, logging
from forms import RegistrationForm, LoginForm, DeleteDForm, DeleteUForm
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
import database
from functools import wraps

app = Flask(__name__)

app.config["SECRET_KEY"] = '\x04\xe7\xf0\x0eS;vdK\xca)\xa6^M\x7f/]Vr\xd4\xff\x81\xbc\xa5'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'projectdb'

mysql = MySQL(app)

HEROKU = False

persons = [
    {
        'firstname': 'Cüneyt',
        'lastname': 'Batırel',
        'title': 'Öğrenci',
        'content': 'Zoom',
        'date': 'November 29, 2020'
    },
    {
        'firstname': 'Ahmet',
        'lastname': 'Öztürk',
        'title': 'Öğretim Üyesi',
        'content': 'Discord',
        'date': 'November 29, 2020'
    }
]

def is_logged_in(f): # Loginse function döndürüyor, değilse login sayfasına yönlendiriyor
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('home'))
        else:
            return f(*args, *kwargs)

    return wrap

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', persons = persons)

@app.route("/deleted", methods = ['GET', 'POST'])
def deleted():
    form = DeleteDForm()
    if form.validate_on_submit():
        named = form.name.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM department WHERE name = '{}'".format(named))
        if(cur.rowcount == 0):
            flash(f'Nothing to delete!', 'danger')
            return redirect(url_for('deleted'))
        cur.execute("DELETE FROM department WHERE name = (%s)", (named,))
        mysql.connection.commit()
        cur.close()
        flash(f'Successfully deleted the department!', 'success')
        return redirect(url_for('deleted'))
    return render_template('deleted.html', title = 'Delete Department', form = form)
    
@app.route("/deleteu", methods = ['GET', 'POST'])
def deleteu():
    form = DeleteUForm()
    if form.validate_on_submit():
        titleu = form.title.data
        cityu = form.city.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM university WHERE title = '{}'".format(titleu))
        if(cur.rowcount == 0):
            flash(f'Nothing to delete!', 'danger')
            return redirect(url_for('deleted'))
        cur.execute("DELETE FROM university WHERE title = (%s)", (titleu,))
        mysql.connection.commit()
        cur.close()
        flash(f'Successfully deleted the university!', 'success')
        return redirect(url_for('deleteu'))
    return render_template('deleteu.html', title = 'Delete University', form = form)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
@not_logged_in
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        usersname = form.username.data
        emails = form.email.data
        phonesnumber = form.phonenumber.data
        firstsname = form.firstname.data
        lastsname = form.lastname.data
        titles = form.title.data
        unis = form.university.data
        cities = form.city.data
        deps = form.department.data
        passwords  = sha256_crypt.encrypt(str(form.password.data))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO UNIVERSITY(title, city) VALUES(%s, %s)", (unis, cities))
        #unid = cur.execute("SELECT id FROM UNIVERSITY WHERE title = %s", (unis,))
        cur.execute("INSERT INTO DEPARTMENT(name) VALUES(%s)", (deps,))
        cur.execute("INSERT INTO PERSON(title, username, email, firstname, lastname, phonenumber, password) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                    (titles, usersname, emails, firstsname, lastsname, phonesnumber, passwords))
        mysql.connection.commit()
        cur.close()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
@not_logged_in
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@log.com' and form.password.data == 'password':
            flash('You have successfully logged in to your account!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Please check your email and password.', 'danger')
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    if (not HEROKU):
        app.run(host="localhost", port=5000, debug=True)
    else:
        app.run()