from app import db

def generate_food_search_query(food_name: str = '', 
	protein_low: float =-1, protein_high: float =-1,
	calorie_low: float =-1, calorie_high: float =-1,
	fat_low: float =-1, fat_high: float =-1,
	carbo_low: float =-1, carbo_high: float =-1) -> str:

	subquery = ''

	if food_name != '':
		keyword_search_query = '(SELECT f.fdc_id FROM Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id WHERE f.Description LIKE \'%%' + food_name + '%%\')'

		subquery += keyword_search_query

	if protein_low != -1 or protein_high != -1:
		protein_filter_query = ('(SELECT f.fdc_id '
														'FROM Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id '
														'WHERE fn.nutrient_id = 1003 AND ')

		if protein_low != -1 and protein_high != -1:
			protein_filter_query += 'fn.Amount >= ' + str(protein_low) + ' AND fn.Amount <= ' + str(protein_high) + ')'
		elif protein_low != -1:
			protein_filter_query += 'fn.Amount >= ' + str(protein_low) + ')'
		else:
			protein_filter_query += 'fn.Amount <= ' + str(protein_high) + ')'

		if subquery != '':
			subquery += ' INTERSECT ' 
			
		subquery += protein_filter_query

	if calorie_low != -1 or calorie_high != -1:
		calorie_filter_query = ('(SELECT f.fdc_id '
														'FROM Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id '
														'WHERE fn.nutrient_id = 1008 AND ')

		if calorie_low != -1 and calorie_high != -1:
			calorie_filter_query += 'fn.Amount >= ' + str(calorie_low) + ' AND fn.Amount <= ' + str(calorie_high) + ')'
		elif calorie_low != -1:
			calorie_filter_query += 'fn.Amount >= ' + str(calorie_low) + ')'
		else:
			calorie_filter_query += 'fn.Amount <= ' + str(calorie_high) + ')'

		if subquery != '':
			subquery += ' INTERSECT ' 

		subquery += calorie_filter_query

	if fat_low != -1 or fat_high != -1:
		fat_filter_query = ('(SELECT f.fdc_id '
												'FROM Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id '
												'WHERE fn.nutrient_id = 1085 AND ')

		if fat_low != -1 and fat_high != -1:
			fat_filter_query += 'fn.Amount >= ' + str(fat_low) + ' AND fn.Amount <= ' + str(fat_high) + ')'
		elif fat_low != -1:
			fat_filter_query += 'fn.Amount >= ' + str(fat_low) + ')'
		else:
			fat_filter_query += 'fn.Amount <= ' + str(fat_high) + ')'

		if subquery != '':
			subquery += ' INTERSECT '

		subquery += fat_filter_query

	if carbo_low != -1 or carbo_high != -1:
		carbo_filter_query = ('(SELECT f.fdc_id '
												  'FROM Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id '
													'WHERE fn.nutrient_id = 1085 AND ')

		if carbo_low != -1 and carbo_high != -1:
			carbo_filter_query += 'fn.Amount >= ' + str(carbo_low) + ' AND fn.Amount <= ' + str(carbo_high) + ')'
		elif carbo_low != -1:
			carbo_filter_query += 'fn.Amount >= ' + str(carbo_low) + ')'
		else:
			carbo_filter_query += 'fn.Amount <= ' + str(carbo_high) + ')'

		if subquery != '':
			subquery += ' INTERSECT '

		subquery += carbo_filter_query

	#TODO The above are subqueries. Write the main query.
	query = ('SELECT f.fdc_id, f.Description, fn.nutrient_id, fn.Amount '
					 'FROM Food f JOIN Food_nutrient fn ON f.fdc_id = fn.fdc_id ')

	if subquery != '':
		query += 'WHERE f.fdc_id IN (' + subquery + ') '

	query += 'ORDER BY f.fdc_id, fn.nutrient_id;'

	return query

def get_food_search_result(food_name: str = '', 
	protein_low: float = -1, protein_high: float = -1,
	calorie_low: float = -1, calorie_high: float = -1,
	fat_low: float = -1, fat_high: float = -1,
	carbo_low: float = -1, carbo_high: float = -1) -> list:
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
			fn_item['food_name'] = result_tuple[1]
			current_fdc_id = result_tuple[0]
		elif current_fdc_id != result_tuple[0]:
			current_fdc_id = result_tuple[0]

			if 'protein' not in fn_item:
				fn_item['protein'] = 'n/a'
			if 'calories' not in fn_item:
				fn_item['calories'] = 'n/a'
			if 'fat' not in fn_item:
				fn_item['fat'] =  'n/a'
			if 'carbohydrate' not in fn_item:
				fn_item['carbohydrate'] = 'n/a'

			food_list.append(fn_item)
			fn_item.clear()
			fn_item['food_name'] = result_tuple[1]

		if result_tuple[2] == 1003:
			fn_item['protein'] = result_tuple[3]
		elif result_tuple[2] == 1008:
			fn_item['calories'] = result_tuple[3]
		elif result_tuple[2] == 1085:
			fn_item['fat'] = result_tuple[3]
		elif result_tuple[2] == 1050:
			fn_item['carbohydrate'] = result_tuple[3]

	if 'protein' not in fn_item:
		print('1 triggered')
		fn_item['protein'] = 'n/a'
	if 'calories' not in fn_item:
		fn_item['calories'] = 'n/a'
	if 'fat' not in fn_item:
		fn_item['fat'] =  'n/a'
	if 'carbohydrate' not in fn_item:
		fn_item['carbohydrate'] = 'n/a'

	food_list.append(fn_item)

	return food_list

def register_user(register_email: str, user_name: str, password: str, 
	first_name: str, last_name: str, date_of_birth: str, sex: int) -> int:
	unique_email_check_query = ('SELECT * '
														  'FROM User_account '
															'WHERE email = \'' + register_email + '\';')

	connection = db.connect()

	unique_check = connection.execute(unique_email_check_query).first()
	if unique_check != None:
		return -1

	user_id_query = ('SELECT MAX(user_id) FROM User_profile;')
	latest_id_check = connection.execute(user_id_query).first()

	print(latest_id_check)

	new_user_id = 1
	if latest_id_check[0] != None:
		new_user_id = latest_id_check[0] + 1


	
	profile_insertion_query = ('INSERT INTO User_profile (user_id, last_name, first_name, date_of_birth, Sex) '
														 'VALUES (' + str(new_user_id) + ', \'' + last_name + '\', \'' + first_name + '\', \'' + date_of_birth + '\', ' + str(sex) + ');')
	# order of insertion: email, user_id, user_name, password
	account_insertion_query = ('INSERT INTO User_account (email, user_id, user_name, password) '
					 									 'VALUES (\'' + register_email + '\', ' + str(new_user_id) + ', \'' + user_name + '\', \'' + password + '\');')

	# order of insertion: user_id, last_name, first_name, date_of_birth, Sex
	# note that the date_of_birth field must be in the form of yyyy-mm-dd 
	
	connection.execute(profile_insertion_query)
	connection.execute(account_insertion_query)
	
	connection.close()

	return new_user_id

def login_user(provided_email: str, provided_pw: str) -> int:
	login_request = ('SELECT user_id '
	                 'FROM User_account '
									 'WHERE email = \'' + provided_email + '\' AND password = \'' + provided_pw + '\';')

	connection = db.connect()
	login_user_id = connection.execute(login_request).first()

	print(login_user_id)

	if login_user_id == None:
		return -1
	else:
		return int(login_user_id[0])

#def update_user(user_id: int, first_name: str, last_name: str, date_of_birth: str, sex: int) -> None:
def update_user_password(user_id: int, password: str) -> None:
    connection = db.connect()
    query = 'Update user_account set password = "{}" where id = {};'.format(password, user_id)
    connection.execute(query)
    connection.close()

def delete_user(user_id: int) -> None:
    ''' remove entries based on user ID 
			  other tables with user_id as foreign key are updated to be on delete cascade.'''
    connection = db.connect()
    account_deletion = 'Delete From user_profile where id={};'.format(user_id)
    connection.execute(account_deletion)
    connection.close()



def get_user_goals(user_id: int) -> None:
	pass  

def add_user_goal(current_weight: float, goal_weight: float) -> None:
	pass

def update_user_goal(user_id: int, goal_id: int) -> None:
	pass

def delete_user_goal(user_id: int, goal_id: int) -> None:
	pass

