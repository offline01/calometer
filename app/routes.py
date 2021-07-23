from app import app
from flask import render_template, request, Response
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

