import os
import psycopg2
from flask import Flask, render_template, g, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") # this connects to heroku database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from sqlalchemy.orm import sessionmaker

# tis part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine(os.getenv("DATABASE_URL"), echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()





# database class
class  Example(Base):
	__tablename__ = "example"
	id = Column(Integer, primary_key=True)
	info = Column(String, )
	name = Column(String, )
	city = Column(String, )




# homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page_2')
def page_2():
	return render_template("random_page_2.html")

@app.route('/hello')
def hello():
	return render_template('hello.html')

# view database page
@app.route('/view_database')
def view_db():
	
	Session = sessionmaker(bind = engine)
	session = Session()
	# the two steps above needed to query database
	data = session.query(Example).all() # name of database class passed in query(...)


	return render_template('view_database.html', data=data)

