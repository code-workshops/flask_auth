"""
Flask Auth

This is a demonstration of how authentication and authorization works. There are also tools in
the python and flask communities that you can use. Study the following:

- models.py: Shows how the user passwords are created and stored
- views.py: Shows how authorization is setup using the session
- _base.html: Shows how authorization is used in the view.

But you should understand how it's generally working!

"""
from flask import Flask, flash, render_template, redirect, request, session
from models import User, connect_to_db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login_view():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user.is_valid_password(password):
        session['user_id'] = user.id
        flash("Login success!")
        return redirect('/')

    flash("Login failed. Try again.")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['user_id'] = None
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    conf_pw = request.form.get('confirm_password')
    if password == conf_pw:
        user = User(email=email, name=name)
        user.create_password(password)
        user.save()

        session['user_id'] = user.id
        return redirect('/')
    else:
        flash('Your passwords do not match.')
        return render_template('signup.html')


if __name__ == '__main__':
    app.secret_key = 'secretzzzz'
    connect_to_db(app)
    app.run()
