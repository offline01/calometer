import time
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='../build', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/food_search', methods=['POST'])
def get_current_time():
    return {'search_result': [{
        'food_name': 'cake1',
        'fat': 11,
        'protein': 12,
        'calories': 13,
        'carbohydrate': 14
    },
    {'food_name': 'cake2',
     'fat': 11,
     'protein': 12,
     'calories': 13,
     'carbohydrate': 14
    }]}

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

    return jsonify({'status': 'success'})

@app.route('/api/user/login', methods=['POST'])
def login():
	if request.method == 'POST':
		login_info = request.get_json()

		email = login_info['email']
		password = login_info['pwd']

	return jsonify({'status': 'success'})

@app.route('/api/user/change_password', methods=['POST'])
def change_pwd():
	if request.method == 'POST':
		pwd_change_info = request.get_json()

		email = pwd_change_info['email']
		old_pwd = pwd_change_info['old_pwd']
		new_pwd = pwd_change_info['new_pwd']
	return jsonify({'status':'success'})

@app.route('/api/user/delete_user', methods=['POST'])
def delete_account():
	if request.method == 'POST':
		target_account = request.get_json()
		target_user_id = target_account['user_id']
	return jsonify({'status': 'success'})