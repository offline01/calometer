from app import app
from flask import render_template, request, Response, redirect, url_for
from app import database as db_helper


@app.route('/', methods=['POST'])
def homepage():
	if request.method == 'POST':
		submitted_search_parameters = request.get_json()

		## somehow grab data from the incoming json\
		name = submitted_search_parameters['name']

		protein_low = submitted_search_parameters['p_low']
		protein_high = submitted_search_parameters['p_high']

		calorie_low = submitted_search_parameters['c_low']
		calorie_high = submitted_search_parameters['c_high']

		fat_low = submitted_search_parameters['f_low']
		fat_high = submitted_search_parameters['f_high']

		carbo_low = submitted_search_parameters['ch_low']
		carbo_high = submitted_search_parameters['ch_high']

		search_result = db_helper.get_food_search_result(name, protein_low, protein_high, calorie_low, calorie_high, fat_low, fat_high, carbo_low, carbo_high)

		return search_result


	return render_template('test_template.html', name='cyka blyat')

@app.route('/register', methods=['POST'])
def register():
	if request.method == 'POST':
		submitted_search_parameters = request.get_json()

		email = submitted_search_parameters['email']
		user_name = submitted_search_parameters['user_name']
		password = submitted_search_parameters['pwd']
		first_name = submitted_search_parameters['f_name']
		last_name = submitted_search_parameters['l_name']
		date_of_birth = submitted_search_parameters['dob']
		sex = submitted_search_parameters['sex']
		
		return redirect(url_for("add_goals"))
	else:
		return render_template('test_template.html', name='cyka blyat')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		submitted_search_parameters = request.get_json()

		email = submitted_search_parameters['email']
		password = submitted_search_parameters['pwd']

		return redirect(url_for("daily_entry"))
	else:
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

