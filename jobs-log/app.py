import os
import psycopg2
from flask import Flask, render_template, g, url_for, request, redirect, flash, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from time import gmtime, strftime

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
class  JobsLog_01(Base):
	__tablename__ = 'jobslog_01'
	id = Column('id', Integer, primary_key=True)
	date = Column('date', String(10))
	time = Column('time', String(5))
	job = Column('job', String(25))
	description = Column('description', String(200))
	outcome = Column('outcome', String(20))
	comments = Column('comments', String(300))
	date_stamp = Column('date_stamp', String(10)) 
	time_stamp = Column('time_stamp', String(5))

	def __init__(self, date, time, job, description, outcome, comments, date_stamp, time_stamp):
		self.date = date
		self.time = time
		self.job = job
		self.description = description
		self.outcome = outcome
		self.comments = comments
		self.date_stamp = date_stamp
		self.time_stamp = time_stamp


Session = sessionmaker(bind=engine)
session = Session()


# homepage
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		#data = session.query(JobsLog_01).all()
		return render_template('homepage.html')
	else:
		date = request.form.get('date_log')
		time = request.form.get('time_log')
		job = request.form.get('job_options')
		description = request.form.get('description')
		outcome = request.form.get('job_outcome')
		comments = request.form.get('comments')
		date_stamp = strftime("%d-%m-%y", gmtime())
		time_stamp = strftime("%H:%M", gmtime())

		db_entry = JobsLog_01(date, time, job, description, outcome, comments, date_stamp, time_stamp)
		session.add(db_entry)
		session.commit()
		data = session.query(JobsLog_01).all()

		#flash(f'log entered: {date_stamp}')
		return render_template('homepage.html', data=data)


# Jobs Report
@app.route('/jobs_report', methods=['GET', 'POST'])
def jobs_report():
	jobs_report = request.form.get('report_options')
	if request.method == 'GET':
		return render_template('jobs_report.html')
	else:
		if jobs_report == "installs":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.job=='installs')			
			install_report = db_entry.all()
			return render_template('jobs_report.html', install_report=install_report)
		elif jobs_report == "maintenance":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.job=='maintenance')
			maintenance_report = db_entry.all()
			return render_template('jobs_report.html', maintenance_report=maintenance_report)
		elif jobs_report == "room_checks":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.job=='room_checks')
			room_report = db_entry.all()
			return render_template('jobs_report.html', room_report=room_report)
		elif jobs_report == "audit_checks":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.job=='audit_checks')
			audit_report = db_entry.all()
			return render_template('jobs_report.html', audit_report=audit_report)
		elif jobs_report == "project_intsalls":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.job=='project_installs')
			project_report = db_entry.all()
			return render_template('jobs_report.html', project_report=project_report)
		else:
			if jobs_report == None:
				return redirect(url_for('home'))


# Outcome Reports
@app.route('/outcome_reports', methods=['GET', 'POST'])
def outcome_reports():
	job_outcome = request.form.get('job_outcome')
	if request.method == 'GET':
		return render_template('outcome_reports.html')
	else:
		if job_outcome == "resolved":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.outcome=='resolved')
			resolved_jobs = db_entry.all()
			return render_template('outcome_reports.html', resolved_jobs=resolved_jobs)
		elif job_outcome == "ongoing":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.outcome=='ongoing')
			ongoing_jobs = db_entry.all()
			return render_template('outcome_reports.html', ongoing_jobs=ongoing_jobs)
		elif job_outcome == "ordered_new_parts":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.outcome=='ordered_new_parts')
			new_parts = db_entry.all()
			return render_template('outcome_reports.html', new_parts=new_parts)

		elif job_outcome == "escalated_3p":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.outcome=='escalate')
			escalate = db_entry.all()
			return render_template('outcome_reports.html', escalate=escalate)

		elif job_outcome == "complete":
			db_entry = session.query(JobsLog_01).filter(JobsLog_01.outcome=='complete')
			finish = db_entry.all()
			return render_template('outcome_reports.html', finish=finish)
		else:
			if job_outcome == None:
				return redirect(url_for('home'))
