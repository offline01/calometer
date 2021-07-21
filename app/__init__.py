import os
import sqlalchemy
from yaml import load, Loader
from flask import Flask, render_template

app = Flask(__name__)


def init_connect_engine():
	if os.environ.get('GAE_ENV') != 'standard':
		# GAE_ENV appears on GCP
		# we are on a local machine here
		variables = load(open('app.yaml'), Loader=Loader)
		env_variables = variables['env_variables']

		for var in env_variables:
			os.environ[var] = env_variables[var]

	pool = sqlalchemy.create_engine(
						sqlalchemy.engine.url.URL(
							drivername='mysql+pymysql',
							username=os.environ.get('MYSQL_USER'), 			# user name
							password=os.environ.get('MYSQL_PASSWORD'), 	# user password
							database=os.environ.get('MTSQL_DB'), 				# db name
							host=os.environ.get('MYSQL_HOST') 					#ip
						)
	)

	return pool

db = init_connect_engine()

connection = db.connect()
# connection.execute()

from app import routes