def get_food_search_result(food_name: str, ) -> dict:
	'''Make the database query with the given parameter'''

	# currently in 
	search_result_list = [
		{
			'name':'ultimate food',
			'protein':1000,
			'calorie':200,
			'fat':0.01,
			'carbohydrate':123,
			'serving size':100
		},
		{
			'name':'ultimate food 2',
			'protein':2000,
			'calorie':400,
			'fat':0.02,
			'carbohydrate':246,
			'serving size':200
		}
	]

	return search_result_list

def register_user(register_email: str, user_name: str, password: str, 
	first_name: str, last_name: str, date_of_birth: str, sex: int) -> None:
	pass

def update_user(user_id: int) -> None:
	pass

def delete_user(user_id: int) -> None:
	pass

def get_user_goals(user_id: int) -> dict:
	pass  

def add_user_goal(current_weight: float, goal_weight: float) -> None:
	pass

def update_user_goal(user_id: int, goal_id: int) -> None:
	pass

def delete_user_goal(user_id: int, goal_id: int) -> None:
	pass

