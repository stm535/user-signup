from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def def_display_signup():
    return render_template('user_signup.html')

@app.route("/", methods=['POST'])
def validate_input():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
        username_error = "Please do not leave this box blank"

    if password == '':
        password_error = "Please do not leave this box blank"

    if verify_password == '':
        verify_password_error = "Please do not leave this box blank"        

    for char in (username):
        if char ==' ':
            username_error = "Username must not contain a space and must be between 3 and 20 characters"
        else:
            if 3>len(username) or len(username)>20:
                username_error = "Username must not contain a space and must be between 3 and 20 characters"

    for char in password:
        if char == ' ':
            password_error = "Password must not contain a space and must be between 3 and 20 characters"
        else:
            if 3>len(password) or len(password)>20:
                password_error = "Password must not contain a space and must be between 3 and 20 characters"

    if password != verify_password:
        verify_password_error = "Passwords do not match"

    if email !='':
        if "@" and "." not in email:
            email_error = "Not a valid email"
        
    if not username_error and not password_error and not verify_password_error and not email_error:
        username=request.form['username']
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('user_signup.html',
        username_error=username_error,
        password_error=password_error,
        verify_password_error=verify_password_error,
        email_error=email_error,
        username=username,
        email=email)    

@app.route("/welcome")
def hello():
    username = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(username)

app.run()
