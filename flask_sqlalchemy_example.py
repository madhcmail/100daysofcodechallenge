from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = ''

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    location = db.Column('location', db.String)
    zipcode = db.Column('zipcode', db.Integer)

    def __init__(self, name,location, zipcode):
        self.name = name
        self.location = location
        self.zipcode = zipcode


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.form['name'] or request.form['location'] or request.form['zipcode']:
            flash('Please enter all the fields', 'error')
        else:
            student = Students(request.form['name'], request.form['location'],request.form['zipcode'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
    return render_template('home.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)




