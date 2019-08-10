Jobs Log TEST

This is a basic web app that creates a table visble for the viewer to see after they submit entries from the homepage.

This file is intended to walk through the step-by-step process I undergone to query my postgres table.

The postgres is being used locally, before setting it up remotely.

# TP-1		[test.py]
AIM:		Set up postgres table through pgAdmin 	

OUTCOME:	table created - "test_table"
			6 columns (id, name, age, profession, city, country)
			REMEMBER!! this is your localhost postgres!


# TP-2		[test.py]
AIM:		set up your flask file - "test.py"

OUTCOME:	quick hello world page to test code
			sql engine & class created for database
			hello world started ok

# TP-3		[test.py]
AIM:		create homepage - choose between enter log or run report 

OUTCOME:	create the base template for my html
			then the homepage (with jinja) & reports page (later)
			inclauded a class for table and put in a variable
			with a few trail & error techniques found a way to add into a table and display back via post method
			** I have noticed that when I exit the page and reload it, the information is lost which means that the data is NOT being committed into the database..

#TP-4		[test.py]
AIM:		make a reports page
			report options = column names
			do a basic report then more detailed later

OUTCOME:	I have realised that the way I set up my log, I won't be able to run a
			report like my original jobs log.  This is becuase I haven't set up options for the user to select.
			By doing this I can only select all from the coloum - just to see if it works.  I will use jinja elif template to give defferent outcomes for each selected column report.
			I used "session.query(database)" to query my database then "order_by(database.id)" to order each entry. After that I can manipulate what I want to reveal in the jinja template when I run a for loop over the database variable.  After that I can easily access the database with "d.id"/"d.name"/"d.city"


CONCLUSION:	I like the way I add data into the database by creating a variable
			for the raw data, then executing the ".add()" method to add the variable into the database class. [lines 48-51 test.py]
			I also like the fact that I can manipulate the report page with the jinja if,elif, else templates; a different page will be generated depending on which the user selects to report.  This saves time from writing out seperate html pages for each report category.
			Then I will have to recreate the profession section and add 4 select
			options: media, catering, security, web developer.  If this works this can be reaaplied to my orginal jobs log.
			This will be in test2.py - I will also include another table displaying the salary (which link both tables with a foreign key).
			test3.py will be when I send the report values (via email) to any given email the user provides.  I suspect all I will have to do is use the "data" variable with Flask-Mail in order to send the data as a csv file.

			REMEMBER!! to connect to my postgres locally I had to create the engine and pass my posgres through it; to connect to your remote postgres you have to import os and include os.getenv() when you pass the postgres through the engine.
			LOCAL 	- 	engine = create_engine("postgresql://username:password@localhost/database", echo = True)
			REMOTE 	- 	engine = create_engine(os.getenv("DATABASE_URL"), echo = True)
			* The DATABASE_URL is your environment variable you can create in Heroku or Bash.

			REMEMBER!! to session.commit() AFTER you session.add(db_entry) !