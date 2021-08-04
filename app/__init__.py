import os
import sqlalchemy
from yaml import load, Loader
from flask import Flask, render_template, request, Response

app = Flask(__name__)

def init_connect_engine() -> sqlalchemy.engine.Engine:
	# if os.environ.get('GAE_ENV') != 'standard':
	# 	# GAE_ENV appears on GCP
	# 	# we are on a local machine here
	# 	variables = load(open('app.yaml'), Loader=Loader)
	# 	env_variables = variables['env_variables']

	# 	for var in env_variables:
	# 		os.environ[var] = env_variables[var]

	pool = sqlalchemy.create_engine(
						# mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
						# sqlalchemy.engine.url.URL(
						# 	drivername='mysql+pymysql',
						# 	username=os.environ.get('MYSQL_USER'), 			# user name
						# 	password=os.environ.get('MYSQL_PASSWORD'), 	# user password
						# 	database=os.environ.get('MTSQL_DB'), 				# db name
						# 	host=os.environ.get('MYSQL_HOST') 					#ip
						# ),
						'mysql+pymysql://root:123456789@127.0.0.1:3306/calometer',
						execution_options={
							"isolation_level": "AUTOCOMMIT"
						}
	)

	return pool

db_engine = init_connect_engine()

from app import database
#print(database.register_user(register_email='fuck@fuck.fuck', user_name='fuck', password='fuckfuckfuck', first_name='fucker', last_name='sucker', date_of_birth='1145-11-19', sex=1))
#print(database.login_user(provided_email='fuck@fuck.fuck', provided_pw='fuckfuckfuck'))
#print(database.update_user_password(email='fuck@fuck.fuck', old_password='fuckthisproject', new_password='fuckthisproject'))
database.delete_user(1)

from app import routes