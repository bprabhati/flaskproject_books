print("__init__.py")
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)

from books_app.book_views import *