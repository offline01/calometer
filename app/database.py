from app import db

def generate_food_search_query(food_name: str, 
	protein_low: float, protein_high: float,
	calorie_low: float, calorie_high: float,
	fat_low: float, fat_high: float,
	carbo_low: float, carbo_high: float) -> str:

	fields = '.fdc_id, f.Description, fn.nutrient_id, fn.Amount'
	tables = 'Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id '
	condition = ''
	if food_name != '':
		condition += 'f.Description LIKE \'%' + food_name + '%\''

	if protein_low != -1 and protein_high != -1:
		condition += ' AND (fn.nutrient_id = 1003 AND fn.Amount >= ' + str(protein_low) + ' AND fn.Amount <= ' + str(protein_high) + ')'
	elif protein_low == -1 and protein_high != -1:
		condition += ' AND (fn.nutrient_id = 1003 AND fn.Amount <= ' + str(protein_high) + ')'
	elif protein_low != -1 and protein_high == -1:
		condition += ' AND (fn.nutrient_id = 1003 AND fn.Amount >= ' + str(protein_low) + ')'

	if calorie_low != -1 and calorie_high != -1:
		condition += ' AND (fn.nutrient_id = 1008 AND fn.Amount >= ' + str(calorie_low) + ' AND fn.Amount <= ' + str(calorie_high) + ')'
	elif calorie_low == -1 and calorie_high != -1:
		condition += ' AND (fn.nutrient_id = 1008 AND fn.Amount <= ' + str(calorie_high) + ')'
	elif calorie_low != -1 and calorie_high == -1:
		condition += ' AND (fn.nutrient_id = 1008 AND fn.Amount >= ' + str(calorie_low) + ')'

	if fat_low != -1 and fat_high != -1:
		condition += ' AND (fn.nutrient_id = 1085 AND fn.Amount >= ' + str(fat_low) + ' AND fn.Amount <= ' + str(fat_high) + ')'
	elif fat_low == -1 and fat_high != -1:
		condition += ' AND (fn.nutrient_id = 1085 AND fn.Amount <= ' + str(fat_high) + ')'
	elif fat_low != -1 and fat_high == -1:
		condition += ' AND (fn.nutrient_id = 1085 AND fn.Amount >= ' + str(fat_low) + ')'

	if carbo_low != -1 and carbo_high != -1:
		condition += ' AND (fn.nutrient_id = 2039 AND fn.Amount >= ' + str(carbo_low) + ' AND fn.Amount <= ' + str(carbo_high) + ')'
	elif carbo_low == -1 and carbo_high != -1:
		condition += ' AND (fn.nutrient_id = 2039 AND fn.Amount <= ' + str(carbo_high) + ')'
	elif carbo_low != -1 and carbo_high == -1:
		condition += ' AND (fn.nutrient_id = 2039 AND fn.Amount >= ' + str(carbo_low) + ')'

	order = 'f.fdc_id'

	query = ('SELECT {fields} '
				 'FROM {tables} '
				 'WHERE {condition} '
				 'ORDER BY {order};')

	return query

def get_food_search_result(food_name: str, 
	protein_low: float, protein_high: float,
	calorie_low: float, calorie_high: float,
	fat_low: float, fat_high: float,
	carbo_low: float, carbo_high: float) -> list:
	'''Make the database query with the given parameter'''

	query = generate_food_search_query(food_name, protein_low, protein_high,
																		 calorie_low, calorie_high, 
																		 fat_low, fat_high,
																		 carbo_low, carbo_high)

	connection = db.connect()
	query_results = connection.execute(query).fetchall()
	connection.close()

	food_list = []

	fn_item = dict()
	current_fdc_id = -1
	for result_tuple in query_results:
		if current_fdc_id == -1:
			fn_item['food name'] = result_tuple[1]
			current_fdc_id = result_tuple[0]
		elif current_fdc_id != result_tuple[0]:
			current_fdc_id = result_tuple[0]
			food_list.append(fn_item)

			fn_item.clear()

			fn_item['food name'] = result_tuple[1]

		if result_tuple[3] == 1003:
			fn_item['protein'] = result_tuple[4]
		elif result_tuple[3] == 1008:
			fn_item['calories'] = result_tuple[4]
		elif result_tuple[3] == 1085:
			fn_item['fat'] = result_tuple[4]
		elif result_tuple[3] == 2039:
			fn_item['carbohydrate'] = result_tuple[4]

	return food_list

def register_user(register_email: str, user_name: str, password: str, 
	first_name: str, last_name: str, date_of_birth: str, sex: int) -> bool:
	unique_email_check_query = ('SELECT * '
														  'FROM User_account '
															'WHERE email = \'' + register_email + '\';')

	connection = db.connect()

	unique_check = connection.execute(unique_email_check_query).first()
	if unique_check == None:
		return False

	user_id_query = ('SELECT MAX(user_id) FROM User_profile;')
	latest_id_check = connection.execute(user_id_query).fetchall()

	new_user_id = 1
	if len(latest_id_check) > 0:
		new_user_id = latest_id_check[0][0] + 1

	# order of insertion: email, user_id, user_name, password
	account_insertion_query = ('INSERT INTO User_account (email, user_id, user_name, password)'
					 									 'VALUES (\'' + register_email + '\', ' + str(new_user_id) + ', \'' + user_name + '\', \'' + password + '\');')

	# order of insertion: user_id, last_name, first_name, date_of_birth, Sex
	# note that the date_of_birth field must be in the form of yyyy-mm-dd 
	profile_insertion_query = ('INSERT INTO User_profile (user_id, last_name, first_name, date_of_birth, Sex)'
														 'VALUES (' + str(new_user_id) + ', \'' + last_name + '\', \'' + first_name + '\', \'' + date_of_birth + '\', ' + str(sex) + ');')

	connection.execute(account_insertion_query)
	connection.execute(profile_insertion_query)

	connection.close()

	return True

#def update_user(user_id: int, first_name: str, last_name: str, date_of_birth: str, sex: int) -> None:
def update_user_password(user_id: int, password: str) -> None:
    connection = db.connect()
    query = 'Update User_account set password = "{}" where id = {};'.format(text, user_id)
    connection.execute(query)
    connection.close()

def delete_user(user_id: int) -> None:
    """ remove entries based on user ID """
    connection = db.connect()
    query = 'Delete From User_account where id={};'.format(user_id)
    connection.execute(query)
    connection.close()

def get_user_goals(user_id: int) -> None:
	pass  

def add_user_goal(current_weight: float, goal_weight: float) -> None:
	pass

def update_user_goal(user_id: int, goal_id: int) -> None:
	pass

def delete_user_goal(user_id: int, goal_id: int) -> None:
	pass

