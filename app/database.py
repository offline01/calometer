#from sqlalchemy.util.langhelpers import set_creation_order
from typing import final
from app import db_engine
from sqlalchemy import exc as execution_exception

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

	connection = db_engine.connect()
	query_results = connection.execute(query).fetchall()
	connection.close()

	# print(query_results)

	food_list = []

	fn_item = dict()
	current_fdc_id = -1
	for result_tuple in query_results:

		if current_fdc_id == -1:
			fn_item['food_name'] = result_tuple[1]
			current_fdc_id = result_tuple[0]
		elif current_fdc_id != result_tuple[0]:

			if 'protein' not in fn_item:
				fn_item['protein'] = 'n/a'
			if 'calories' not in fn_item:
				fn_item['calories'] = 'n/a'
			if 'fat' not in fn_item:
				fn_item['fat'] =  'n/a'
			if 'carbohydrate' not in fn_item:
				fn_item['carbohydrate'] = 'n/a'

			food_list.append(fn_item)
			del fn_item
			fn_item = dict()
			current_fdc_id = result_tuple[0]
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
		fn_item['protein'] = 'n/a'
	if 'calories' not in fn_item:
		fn_item['calories'] = 'n/a'
	if 'fat' not in fn_item:
		fn_item['fat'] =  'n/a'
	if 'carbohydrate' not in fn_item:
		fn_item['carbohydrate'] = 'n/a'

	food_list.append(fn_item)

	print(food_list)

	return food_list

def register_user(register_email: str, user_name: str, password: str, 
	first_name: str, last_name: str, date_of_birth: str, sex: int) -> int:
	new_id = 0
	register_query = 'CALL register_user(\'' + register_email + '\', \'' + user_name + '\', \'' + password + '\', \'' + first_name + '\', \'' + last_name + \
		'\', \'' + date_of_birth + '\', ' + str(sex) + ', @new_user_id);'
	result_query = 'SELECT @new_user_id;'
	
	connection = db_engine.connect()
	try:	
		connection.execute(register_query)
		result = connection.execute(result_query).first()

		new_id = result[0]
	except execution_exception.IntegrityError: 
		new_id = -2
	except:
	 	new_id = -1

	return new_id

def login_user(provided_email: str, provided_pw: str) -> int:
	login_request = 'CALL login_user(\'' + provided_email + '\', \'' + provided_pw + '\', @curr_user_id);'
	result_query = 'select @curr_user_id;'

	login_user_id = 0

	connection = db_engine.connect()
	try:
		connection.execute(login_request)
		result = connection.execute(result_query).first()
		login_user_id = result[0]
	except:
		login_user_id = -1
	finally:
		connection.close()

	return login_user_id

def update_user_password(email: str, old_password: str, new_password: str) -> int:
	status = 0
	update_query = 'CALL update_user_password(\'' + email + '\', \'' + old_password + '\', \'' + new_password + '\', @stat);'
	status_query = 'select @stat;'

	connection = db_engine.connect()
	try:
		connection.execute(update_query)
		result = connection.execute(status_query).first()
		status = result[0]
	except:
		status = -1
	finally:
		connection.close()

	return status

def delete_user(user_id: int) -> None:
	deletion_query = 'CALL delete_user(' + str(user_id) + ');'

	connection = db_engine.connect()
	try:
		connection.execute(deletion_query)
	except:
		pass
	finally:
		connection.close()

def advanced_query_1() -> None:
	pass

def advanced_query_2() -> None:
	pass