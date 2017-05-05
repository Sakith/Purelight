**This is a purelight test projet wchis is written is python and its compient framework Django this suppose to run on google appengine with Nginx,GUniconn and mysql.

Before run application create database called purelightDB on you runiing database instance and update settings.py according to that settings.**


===========================================================
**
### How to setup dev enviroment ###**

1. clone in to purelight source
2. run command
 		cd purelight/
 		pip install virtualenv
 		virtualenv purlight-env
		source purelight-env/bin/activate
		cd /purelight
		pip install -r reqirement.txt

3.then checkout to develop branch and branch out youe feature branch from develop
	branch naming convention would be feature/<youname-in-lower-case>/<feature-name>


**### How to set up database ###**

1. sudo apt-get install mysql-server
2. sudo apt-get install python-setuptools python-dev build-essential
3. source myenv/bin/activate
4. sudo apt-get install libmysqlclient-dev
5. pip install MySQL-python

then go to mysql console using

1. mysql -u <dbusesr> -p <dbpassword>
2. creat Database purelightDB

=======================================================================================