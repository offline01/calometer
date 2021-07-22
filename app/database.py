from app import db

def get_food_search_result(food_name: str, 
	protein_low: float, protein_high: float,
	calorie_low: float, calorie_high: float,
	fat_low: float, fat_high: float,
	carbo_low: float, carbo_high: float) -> list:
	'''Make the database query with the given parameter'''

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

	connection = db.connect()
	query_results = connection.execute(query).fetchall()

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
	first_name: str, last_name: str, date_of_birth: str, sex: int) -> None:
	pass

def update_user(user_id: int) -> None:
	pass

def delete_user(user_id: int) -> None:
	pass

def get_user_goals(user_id: int) -> None:
	pass  

def add_user_goal(current_weight: float, goal_weight: float) -> None:
	pass

def update_user_goal(user_id: int, goal_id: int) -> None:
	pass

def delete_user_goal(user_id: int, goal_id: int) -> None:
	pass

