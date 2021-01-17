from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

persons = [
    {
        'firstname': 'Cüneyt',
        'lastname': 'Batırel',
        'title': 'Student',
        'content': 'Zoom',
        'date': 'November 29, 2020'
    },
    {
        'firstname': 'Ahmet',
        'lastname': 'Yılmaz',
        'title': 'Lecturer',
        'content': 'Discord',
        'date': 'November 29, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', persons = persons)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
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
    app.run(debug = True)