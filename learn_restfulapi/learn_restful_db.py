from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_1.db"

db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    def __init__(self, name, location):
        self.name = name
        self.location = location


if __name__ == '__main__':
    db.create_all()
    customer_1 = Customer('madhuri', 'Arkansas')
    customer_2 = Customer('John', 'St.Louis')

    db.session.add(customer_1)
    db.session.add(customer_2)
    db.session.commit()
    app.run(debug=True)