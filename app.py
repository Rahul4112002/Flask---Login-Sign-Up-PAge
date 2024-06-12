from flask import Flask,render_template,redirect,url_for,flash
from forms import SignupForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = "this_is_a_secret_key"
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Home")

@app.route("/signup",methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully Registered {form.username.data}!")
        return redirect(url_for("home"))
    return render_template('signup.html',form=form,title="Sign Up")

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        if email=='rahul@gmail.com' and pw=='Rahul123':
            flash(f"Successfully Login!")
            return redirect(url_for("home"))
        else:
            flash(f'Incorrect Email and Password')
    return render_template('login.html',form=form,title='Login')

if __name__ == '__main__':
    app.run(debug=True)