from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# secret_key is required for application when creating Forms to protect cookies, cross-site attcks, forgeries
# generate a random key using secrets module
app.config['SECRET_KEY'] = '1a700710114e598f9e01932bc41ed313'

posts = [
    {
        'author': 'Madhuri',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'June 26, 2020'
    },
    {
        'author': 'Madhuri',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 26, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
