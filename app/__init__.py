import os
import sqlalchemy
from yaml import load, Loader
from flask import Flask, render_template, request, Response

app = Flask(__name__)


def init_connect_engine() -> sqlalchemy.engine.Engine:
	if os.environ.get('GAE_ENV') != 'standard':
		# GAE_ENV appears on GCP
		# we are on a local machine here
		variables = load(open('app.yaml'), Loader=Loader)
		env_variables = variables['env_variables']

		for var in env_variables:
			os.environ[var] = env_variables[var]

	db_config = {
        # [START cloud_sql_mysql_sqlalchemy_limit]
        # Pool size is the maximum number of permanent connections to keep.
        "pool_size": 5,
        # Temporarily exceeds the set pool_size if no connections are available.
        "max_overflow": 2,
        # The total number of concurrent connections for your application will be
        # a total of pool_size and max_overflow.
        # [END cloud_sql_mysql_sqlalchemy_limit]

        # [START cloud_sql_mysql_sqlalchemy_backoff]
        # SQLAlchemy automatically uses delays between failed connection attempts,
        # but provides no arguments for configuration.
        # [END cloud_sql_mysql_sqlalchemy_backoff]

        # [START cloud_sql_mysql_sqlalchemy_timeout]
        # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
        # new connection from the pool. After the specified amount of time, an
        # exception will be thrown.
        "pool_timeout": 30,  # 30 seconds
        # [END cloud_sql_mysql_sqlalchemy_timeout]

        # [START cloud_sql_mysql_sqlalchemy_lifetime]
        # 'pool_recycle' is the maximum number of seconds a connection can persist.
        # Connections that live longer than the specified amount of time will be
        # reestablished
        "pool_recycle": 1800,  # 30 minutes
        # [END cloud_sql_mysql_sqlalchemy_lifetime]

    }

	pool = sqlalchemy.create_engine(
						# mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
						# sqlalchemy.engine.url.URL(
						# 	drivername='mysql+pymysql',
						# 	username=os.environ.get('MYSQL_USER'), 			# user name
						# 	password=os.environ.get('MYSQL_PASSWORD'), 	# user password
						# 	database=os.environ.get('MTSQL_DB'), 				# db name
						# 	host=os.environ.get('MYSQL_HOST') 					#ip
						# ),
						'mysql+pymysql://root:@34.135.179.50:3306/calometer',

						**db_config
	)

	return pool

db = init_connect_engine()

# connection = db.connect()
# results = connection.execute('select * from Food limit 5;').fetchall()
# print([x for x in results])
# connection.close()

from app import routes