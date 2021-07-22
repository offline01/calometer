from app import app
from flask import render_template
#from app import database as db_helper

@app.route('/')
def homepage():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/register')
def register():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/login')
def login():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/goals')
def goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/goals/add_goals')
def add_goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/goals/daily_entry')
def daily_entry():
	return render_template('test_template.html', name='cyka blyat')

