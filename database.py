import mysql.connector as conman

db = conman.connect(host = "localhost", user = "root", password = "password") 

cursorobj = db.cursor()
cursorobj.execute("CREATE DATABASE IF NOT EXISTS PROJECTDB")

# connecting to the database 
db = conman.connect(host = "localhost", user = "root", password = "password", database = "projectdb") 

# preparing a cursor object 
cursorobj = db.cursor() 

# creating tables 
createuni =  """CREATE TABLE IF NOT EXISTS UNIVERSITY ( 
				ID INTEGER PRIMARY KEY AUTO_INCREMENT, 
				TITLE VARCHAR(255) NOT NULL, 
				CITY VARCHAR(50) NOT NULL
				);"""

createdep =  """CREATE TABLE IF NOT EXISTS DEPARTMENT ( 
				ID INTEGER PRIMARY KEY AUTO_INCREMENT, 
				NAME VARCHAR(255) NOT NULL, 
				UNIVERSITYID INTEGER,
				FOREIGN KEY (UNIVERSITYID) REFERENCES UNIVERSITY(ID)
				);"""

createperson = """CREATE TABLE IF NOT EXISTS PERSON (
				ID INTEGER PRIMARY KEY AUTO_INCREMENT,
				TITLE VARCHAR(50) NOT NULL,
				USERNAME VARCHAR(50) NOT NULL UNIQUE,
				EMAIL VARCHAR(50) NOT NULL UNIQUE,
				FIRSTNAME VARCHAR(50) NOT NULL,
				LASTNAME VARCHAR(50) NOT NULL,
				PHONENUMBER VARCHAR(10) NOT NULL UNIQUE,
				PASSWORD VARCHAR(300) NOT NULL,
				UNIVERSITYID INTEGER,
				FOREIGN KEY (UNIVERSITYID) REFERENCES UNIVERSITY(ID)
				);"""

createmeeting = """CREATE TABLE IF NOT EXISTS MEETING (
				ID INTEGER PRIMARY KEY AUTO_INCREMENT,
				PLATFORM VARCHAR(50) NOT NULL,
				ISCONDUCTED BOOLEAN DEFAULT FALSE,
				PERSONID INTEGER,
				FOREIGN KEY (PERSONID) REFERENCES PERSON(ID)
				);"""

createtimeblock = """CREATE TABLE IF NOT EXISTS TIMEBLOCK (
					ID INTEGER PRIMARY KEY AUTO_INCREMENT,
					TIMEFRAME TIME,
					ISAVAILABLE BOOLEAN DEFAULT FALSE,
					DATE DATE,
					NAME VARCHAR(255) NOT NULL,
					PERSONID INTEGER,
					FOREIGN KEY (PERSONID) REFERENCES PERSON(ID)
					);"""


# table created
cursorobj.execute(createuni)
cursorobj.execute(createdep)
cursorobj.execute(createperson)
cursorobj.execute(createtimeblock) 
cursorobj.execute(createmeeting) 

# disconnecting from server
db.close()








