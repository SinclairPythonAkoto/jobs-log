Jobs Log

This is a basic web app that creates a table visble for the viewer to see after they submit entries from the homepage.

When the user submits their entry, it is stored into a database; it is then sent back to the page (from the database) in order for the user to view.

My previous version of this used SQLite3 and ran the app locally; now I will be using PostgreSQL and running the app remotely.

In the TEST folder you can find test.py which is basically a test app to test how I will query the database (with SQLAlchemy); the PostgreSQL database will be ran locally before setting up the remote on Heroku.  This app can be executed through the command line (in my PowerShell.)  You can also find a 'thought-process.txt' file which you can read through my trail & error processes when testing my query methods.

