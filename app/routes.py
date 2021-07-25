from app import app
from flask import json, render_template, request, jsonify
import json
from app import database as db_helper

@app.route('/api/test_response', methods=['POST'])
def test_response():
	test_info = request.get_json()

	print(test_info)

	return jsonify({'fuck':'you', 'cyka':'blyat', 'wdnmd':'nmsl', 'sent':test_info['sent']})

@app.route('/api/food_search', methods=['POST'])
def search_food():
	if request.method == 'POST':
		submitted_search_parameters = request.get_json()

		print(submitted_search_parameters)

		name = submitted_search_parameters['name']

		protein_low = float( submitted_search_parameters['p_low'] )
		protein_high = float( submitted_search_parameters['p_high'] )

		calorie_low = float(submitted_search_parameters['c_low'] )
		calorie_high = float(submitted_search_parameters['c_high'] )

		fat_low = float(submitted_search_parameters['f_low'] )
		fat_high = float(submitted_search_parameters['f_high'] )

		carbo_low = float(submitted_search_parameters['ch_low'] )
		carbo_high = float(submitted_search_parameters['ch_high'] )

		search_result = db_helper.get_food_search_result(name, protein_low, protein_high, calorie_low, calorie_high, fat_low, fat_high, carbo_low, carbo_high)

		return jsonify({'status':'success', 'search_result': search_result})

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
			return jsonify({'status': 'success', 'new_user_id': new_user_id})
		else:
			return jsonify({'status': 'failed'})

@app.route('/api/user/login', methods=['POST'])
def login():
	if request.method == 'POST':
		login_info = request.get_json()

		email = login_info['email']
		password = login_info['pwd']

		logged_in_user_id = db_helper.login_user(email, password)

		if logged_in_user_id != -1:
			return jsonify({'status': 'success', 'current_user': logged_in_user_id})
		else:
			return jsonify({'status': 'failed'})

@app.route('/api/user/change_password', methods=['POST'])
def change_pwd():
	if request.method == 'POST':
		pwd_change_info = request.get_json()

		email = pwd_change_info['email']
		new_pwd = pwd_change_info['pwd']

		db_helper.update_user_password(email, new_pwd)

		return jsonify({'status': 'success'})

@app.route('/api/user/delete_user', methods=['POST'])
def delete_account():
	if request.method == 'POST':

		target_account = request.get_json()

		target_user_id = target_account['user_id']

		db_helper.delete_user(target_user_id)

		return jsonify({'status': 'success'})	

@app.route('/api/goals/get_user_goals', methods=['POST'])
def goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/api/goals/add_goals', methods=['POST'])
def add_goals():
	return render_template('test_template.html', name='cyka blyat')

@app.route('/api/goals/get_daily_entry', methods=['POST'])
def daily_entry():
	return render_template('test_template.html', name='cyka blyat')

