from flask import Flask, render_template, g, url_for, request, redirect

app = Flask(__name__)

from sqlalchemy.orm import sessionmaker

# # this part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
meta = MetaData()
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:161086@localhost/test-db-01", echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# database class
class  Test_db_01(Base):
	__tablename__ = "test_table"
	id = Column('id', Integer, primary_key=True)
	name = Column('name', String(40),)
	age = Column('age', Integer,)
	profession = Column('profession', String(60),)
	city = Column('city', String(60),)
	country = Column('country', String(40),)

	def __init__(self, name, age, profession, city, country):
		self.name = name
		self.age = age
		self.profession = profession
		self.city = city
		self.country = country

Session = sessionmaker(bind=engine)
session = Session()

# homepage
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		data = session.query(Test_db_01).all()
		return render_template('homepage.html')
	else:
		name = request.form.get('name')
		age = request.form.get('age')
		profession = request.form.get('profession')
		city = request.form.get('city')
		country = request.form.get('country')

		db_entry = Test_db_01(name, age, profession, city, country)
		session.add(db_entry)
		session.commit()
		data = session.query(Test_db_01).all()

		return render_template('homepage.html', data=data)

# report page
@app.route('/reports', methods=['GET', 'POST'])
def reports():
	if request.method == 'GET':
		return render_template('reports.html')
	else:
		if request.form.get("report_options") == "name":
			db_entry = session.query(Test_db_01).order_by(Test_db_01.id)
			data_name = db_entry.all()
			return render_template('reports.html', data_name=data_name)
		elif request.form.get("report_options") == "age":
			db_entry = session.query(Test_db_01).order_by(Test_db_01.id)
			data_age = db_entry.all()
			return render_template('reports.html', data_age=data_age)
		elif request.form.get("report_options") == "profession":
			db_entry = session.query(Test_db_01).order_by(Test_db_01.id)
			data_prof = db_entry.all()
			return render_template('reports.html', data_prof=data_prof)
		elif request.form.get("report_options") == "city":
			db_entry = session.query(Test_db_01).order_by(Test_db_01.id)
			data_city = db_entry.all()
			return render_template('reports.html', data_city=data_city)
		elif request.form.get("report_options") == "country":
			db_entry = session.query(Test_db_01).order_by(Test_db_01.id)
			data_country = db_entry.all()
			return render_template('reports.html', data_country=data_country)
		else:
			# this redirects you back to page if
			# button pressed without selecting a category to run
			return redirect(url_for('reports'))



if __name__ == '__main__':
	app.run(debug=True)