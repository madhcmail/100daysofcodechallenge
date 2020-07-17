from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# secret_key is required for application when creating Forms to protect cookies, cross-site attacks, forgeries
# generate a random key using secrets module
app.config['SECRET_KEY'] = '1a700710114e598f9e01932bc41ed313'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes