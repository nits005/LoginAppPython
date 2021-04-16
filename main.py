from flask import Flask, render_template, flash, request
from wtforms import Form, StringField, PasswordField, validators

application = Flask(__name__)
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '123456'

fixed_user = 'Nitin'
fixed_password = 'password'

class LoginForm(Form):
    username = StringField('Username:',   validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])


@application.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if form.validate():
            if username == fixed_user and password == fixed_password:
                flash('Login Successful!')
            else:
                flash('Error: Login failed due to incorrect Username or Password')
        else:
            flash('Error: Username & Password are manadatory')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=8080, debug=True)