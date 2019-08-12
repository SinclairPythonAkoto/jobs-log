from flask import Flask, render_template, g, url_for, request, redirect

app = Flask(__name__)

from sqlalchemy.orm import sessionmaker, relationship

# # this part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
meta = MetaData()
engine = create_engine("postgresql://postgres:161086@localhost/test-db-01", echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# database class
class  Test3_table(Base):
	__tablename__ = 'test3_table'
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

class Salary(Base):
	__tablename__ = 'salary'
	id = Column('id', Integer, primary_key=True)
	wage = Column('wage', String(20))



Session = sessionmaker(bind=engine)
session = Session()

# homepage
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		data = session.query(Test3_table).all()
		return render_template('homepage.html')
	else:
		date_log = request.form.get('date_log')
		name = request.form.get('name')
		age = request.form.get('age')
		profession = request.form.get('profession')
		city = request.form.get('city')
		country = request.form.get('country')

		db_entry = Test3_table(name, age, profession, city, country)
		session.add(db_entry)
		session.commit()
		data = session.query(Test3_table).all()

		return render_template('homepage.html', data=data)

# report page
@app.route('/reports', methods=['GET', 'POST'])
def reports():
	#email_btn = request.form.get("email_btn")
	if request.method == 'GET':
		return render_template('reports.html')
	else:
		report_btn = request.form.get("report_btn")
		email = request.form.get("email")
		email_btn = request.form.get("email_btn")
		confirm_email = request.form.get("confirm_email")
		report_options = request.form.get("report_options")


		# if email != None and request.form.get("report_options") == None:
		# 		return f"{email} was sent from the report page."

		# if NO email & NO report options selected 
		# if request.form.get("report_options") == None and email == None:
		# 	return redirect(url_for('home'))
		# # if NO report options selected
		# elif email != None and request.form.get("report_options") == None:
		# 	return redirect(url_for('reports'))

		if report_options == None:# and email == None:
			return redirect(url_for('reports'))
		else:
			if report_options == "name":
				db_entry = session.query(Test3_table).order_by(Test3_table.id)
				data_name = db_entry.all()
				return render_template('reports.html', data_name=data_name)
			elif report_options == "age":
				db_entry = session.query(Test3_table).order_by(Test3_table.id)
				data_age = db_entry.all()
				return render_template('reports.html', data_age=data_age)		
			elif report_options == "media_prof":
				db_entry = session.query(Test3_table).order_by(Test3_table.id).filter(Test3_table.profession=='media')
				media_prof = db_entry.all()
				return render_template('reports.html', media_prof=media_prof)
			elif report_options == "catering_prof":
				db_entry = session.query(Test3_table).filter(Test3_table.profession=='catering')
				catering_prof = db_entry.all()
				return render_template('reports.html', catering_prof=catering_prof)
			elif report_options == "security_prof":
				db_entry = session.query(Test3_table).filter(Test3_table.profession=='security')
				security_prof = db_entry.all()
				return render_template('reports.html', security_prof=security_prof)

			elif report_options == "web_prof":
				db_entry = session.query(Test3_table).filter(Test3_table.profession=='security')
				web_prof = db_entry.all()
				# change it to confirm email; if both values match then proceed below..			
				
				if email in request.form:
					return redirect(url_for('home'))
				return render_template('reports.html', web_prof=web_prof)
				
			elif report_options == "city":
				db_entry = session.query(Test3_table).order_by(Test3_table.id)
				data_city = db_entry.all()
				return render_template('reports.html', data_city=data_city)
			elif report_options == "country":
				db_entry = session.query(Test3_table).order_by(Test3_table.id)
				data_country = db_entry.all()
				return render_template('reports.html', data_country=data_country)
			elif report_options == "all_db":
				db_entry = session.query(Test3_table).order_by(Test3_table.id)
				db_entry = db_entry.all()
				return render_template('reports.html', db_entry=db_entry)

			# else:
			# 	if report_options == None:# and email == None:
			# 		return redirect(url_for('reports'))
			# 	elif email == confirm_email:#and report_options == None:
			# 		return "RANDOM MESSAGE!"
					#return redirect(url_for('home'))
			

		# else:
		# 	return f"{email} was sent from the report page."
		# else:
		# 	try:
		# 		if email == None:
		# 			return redirect(url_for('reports'))
		# 	except:
		# 		return "there is an error somewhere in your code."
		# 	else:
		# 		return f"{email} was sent from the report page."
			# finally:
			# 	pass
			# return redirect(url_for('home'))
			# this redirects you back to page if
				# button pressed without selecting a category to run
					#return redirect(url_for('reports'))


if __name__ == '__main__':
	app.run(debug=True)
