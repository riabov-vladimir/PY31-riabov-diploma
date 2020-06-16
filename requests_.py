import requests
from pprint import pprint
import time

access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


def user_id_str_to_int(user_id: str) -> int:
	"""
	функция принимающая screen_name и возвращающая числовой id пользовтаеля
	"""

	request_url = 'https://api.vk.com/method/users.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_ids': user_id,
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response'][0]['id']
	return json_


def get_int_id(user_id='arbore'):
	"""
	Логика позволяющая принимать в качестве user_id как числовой идентификатор, так и screen_name
	"""

	if type(user_id) == int:
		return user_id
	elif type(user_id) == str:
		return user_id_str_to_int(user_id)


def friends_get(user_id: int) -> list:

	"""функция возвращающая список друзей пользовтаеля"""

	request_url = 'https://api.vk.com/method/friends.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		'count': 1000,
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_


def groups_get(user_id: int) -> list:

	"""функция возвразающая список групп, в которых состоит пользователь"""

	request_url = 'https://api.vk.com/method/groups.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		'count': 500
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_


def groups_is_member(group_id: str, user_ids: list):

	"""Состоит ли пользователь в сообществе"""

	request_url = 'https://api.vk.com/method/groups.isMember'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_id': group_id,
		'user_ids': str(user_ids)[1:-1:]
	}

	response = requests.get(request_url, params=params)

	json_ = response.json()['response']

	return json_


groups_test = [45491419, 140105161, 88350989, 95648824, 33621085, 164765862, 144822899, 78920715, 29534144, 26750264,
			55404958, 72188644, 63731512, 90464514, 137153726, 91421416]


def groups_list_info(groups_list: list):

	request_url = 'https://api.vk.com/method/groups.getById'

	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_ids': str(groups_list)[1:-1:],
		'fields': 'members_count'
	}

	response = requests.get(request_url, params=params)

	json_ = response.json()['response']

	return json_


if __name__ == "__main__":
	pprint(groups_get(171691064))
	pprint(groups_is_member('8564', groups_test))
