from app import app
from flask import render_template, request, Response, redirect, url_for
from app import database as db_helper


@app.route('/api/food_search', methods=['POST'])
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

@app.route('/api/user/register', methods=['POST'])
def register():
	if request.method == 'POST':

		user_info = request.get_json()

		email = user_info['email']
		user_name = user_info['user_name']
		password = user_info['pwd']
		first_name = user_info['f_name']
		last_name = user_info['l_name']
		date_of_birth = user_info['dob']
		sex = user_info['sex']

		new_user_id = db_helper.register_user(email, user_name, password, first_name, last_name, date_of_birth, sex)
		if new_user_id != -1:
			return {'new_user_id': str(new_user_id)}
		else:
			return {'new_user_id': 'Failed'}
		
		# return redirect(url_for("add_goals"))
	else:
		return render_template('test_template.html', name='cyka blyat')

@app.route('/api/user/login', methods=['POST'])
def login():
	if request.method == 'POST':
		login_info = request.get_json()

		email = login_info['email']
		password = login_info['pwd']

		logged_in_user_id = db_helper.login_user(email, password)

		if logged_in_user_id == -1:
			return {'current_user': 'failed'}
		else:
			return {'current_user': str(logged_in_user_id)}

	else:
		return render_template('test_template.html', name='cyka blyat')

@app.route('/api/user/change_password')

@app.route('/api/goals/get_user_goals', methods=['POST'])
def goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/api/goals/add_goals', methods=['POST'])
def add_goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/api/goals/get_daily_entry', methods=['POST'])
def daily_entry():
	return render_template('test_template.html', name='cyka blyat')

