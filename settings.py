from flask import Flask
import os

app = Flask(__name__)

database_file = os.getcwd() + '/database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(database_file)