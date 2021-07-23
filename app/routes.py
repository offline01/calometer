from app import app
from flask import render_template, request, Response
from app import database as db_helper


@app.route('/', methods=['GET', 'POST'])
def homepage():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/goals', methods=['GET', 'POST'])
def goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/goals/add_goals', methods=['GET', 'POST'])
def add_goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/goals/daily_entry', methods=['GET', 'POST'])
def daily_entry():
	return render_template('test_template.html', name='cyka blyat')

