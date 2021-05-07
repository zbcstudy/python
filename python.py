from flask import Flask
from forms import LoginForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/user/<name>")
def user(name):
    return '<h1>hello %s!</h1>' % name

@app.route('login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('username:' + form.username.data)
        return render_template('index.html', form=form)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
