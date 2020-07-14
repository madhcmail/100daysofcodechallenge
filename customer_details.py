from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SECRET_KEY'] = ''

db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    location = db.Column('location', db.String)
    zipcode = db.Column('zipcode', db.String)

    def __init__(self, name, location, zipcode):
        self.name = name
        self.location = location
        self.zipcode = zipcode


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['location'] or not request.form['zipcode']:
            flash("Please enter all the fields", 'error')

        else:
            customer = Customer(request.form['name'], request.form['location'], request.form['zipcode'])

            db .session.add(customer)
            db.session.commit()
            flash("Record added successfully")
    return render_template('home.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


