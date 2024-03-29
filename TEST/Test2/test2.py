from flask import Flask, render_template, g, url_for, request, redirect

app = Flask(__name__)

from sqlalchemy.orm import sessionmaker, relationship

# # this part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
meta = MetaData()
engine = create_engine("postgresql://postgres:161086@localhost/test-db-01", echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# database class
class  Test_db_02(Base):
	__tablename__ = 'test2_table'
	id = Column('id', Integer, primary_key=True)
	date = Column('date', String(10))
	name = Column('name', String(40),)
	age = Column('age', Integer,)
	profession = Column('profession', String(60),)
	city = Column('city', String(60),)
	country = Column('country', String(40),)	

	def __init__(self, date, name, age, profession, city, country):
		self.date = date
		self.name = name
		self.age = age
		self.profession = profession
		self.city = city
		self.country = country

class Salary(Base):
	__tablename__ = 'salary'
	id = Column('id', Integer, primary_key=True)
	wage = Column('wage', String(20))
	test2_id = Column('test2_id' ,Integer, ForeignKey('test2_table.id'))
	
	wages = relationship("Test_db_02", backref="salary", primaryjoin="Test_db_02.id == Salary.test2_id")

Session = sessionmaker(bind=engine)
session = Session()

# homepage
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		data = session.query(Test_db_02).all()
		return render_template('homepage.html')
	else:
		date_log = request.form.get('date_log')
		name = request.form.get('name')
		age = request.form.get('age')
		profession = request.form.get('profession')
		city = request.form.get('city')
		country = request.form.get('country')

		db_entry = Test_db_02(date_log,name, age, profession, city, country)
		session.add(db_entry)
		session.commit()
		data = session.query(Test_db_02).all()

		return render_template('homepage.html', data=data)

# report page
@app.route('/reports', methods=['GET', 'POST'])
def reports():
	if request.method == 'GET':
		return render_template('reports.html')
	else:
		if request.form.get("report_options") == "name":
			db_entry = session.query(Test_db_02).order_by(Test_db_02.id)
			data_name = db_entry.all()
			return render_template('reports.html', data_name=data_name)
		elif request.form.get("report_options") == "age":
			db_entry = session.query(Test_db_02).order_by(Test_db_02.id)
			data_age = db_entry.all()
			return render_template('reports.html', data_age=data_age)

		elif request.form.get("report_options") == "media_prof":
			db_entry = session.query(Test_db_02).join(Test_db_02.salary).filter(Test_db_02.profession=='media') # this works but only salary object given back			
			media_prof = db_entry.all()
			return render_template('reports.html', media_prof=media_prof)


		elif request.form.get("report_options") == "catering_prof":
			db_entry = session.query(Test_db_02).filter(Test_db_02.profession=='catering')
			catering_prof = db_entry.all()
			return render_template('reports.html', catering_prof=catering_prof)
		elif request.form.get("report_options") == "security_prof":
			db_entry = session.query(Test_db_02).filter(Test_db_02.profession=='security')
			security_prof = db_entry.all()
			return render_template('reports.html', security_prof=security_prof)
		elif request.form.get("report_options") == "web_prof":
			db_entry = session.query(Test_db_02).filter(Test_db_02.profession=='security')
			web_prof = db_entry.all()
			return render_template('reports.html', web_prof=web_prof)

		elif request.form.get("report_options") == "city":
			db_entry = session.query(Test_db_02).order_by(Test_db_02.id)
			data_city = db_entry.all()
			return render_template('reports.html', data_city=data_city)
		elif request.form.get("report_options") == "country":
			db_entry = session.query(Test_db_02).order_by(Test_db_02.id)
			data_country = db_entry.all()
			return render_template('reports.html', data_country=data_country)
		elif request.form.get("report_options") == "all_db":
			db_entry = session.query(Test_db_02).order_by(Test_db_02.id)
			db_entry = db_entry.all()
			return render_template('reports.html', db_entry=db_entry)
		else:
			# this redirects you back to page if
			# button pressed without selecting a category to run
			return redirect(url_for('reports'))


if __name__ == '__main__':
	app.run(debug=True)
