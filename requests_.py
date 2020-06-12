import requests
from pprint import pprint
import time

access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008' # scope_friends


def user_id_str_to_int(user_id: str) -> int:

	"""функция принимающая screen_name и возвращающая числовой id пользовтаеля"""

	request_url = 'https://api.vk.com/method/users.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_ids': user_id,
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response'][0]['id']
	return json_



def friends_get(user_id: int) -> list:

	"""функция возвращающая список друзей пользовтаеля"""

	request_url = 'https://api.vk.com/method/friends.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		#'count': 10,
		# 'order': 'name'
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
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_


def members_get(group_id: str) -> list:

	"""функция возвращающая список участников сообщества"""

	request_url = 'https://api.vk.com/method/groups.getMembers'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_id': group_id,
	}

	response = requests.get(request_url, params=params)
	json_ = response.json() # ['response']['items']
	return json_


def members_get_friends(group_id: str, user_id: int or str) -> list: # ????

	request_url = 'https://api.vk.com/method/groups.getMembers'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_id': group_id,
		'filter': 'friends',
		'user_id': user_id
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_


def groups_isMember(group_id: str, user_id: int):

	"""Состоит ли пользователь в сообществе"""

	request_url = 'https://api.vk.com/method/groups.isMember'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_id': group_id,
		# 'user_ids': None,
		'user_id': user_id
	}

	response = requests.get(request_url, params=params)
	json_ = response.json() #['response']
	return json_


# pprint(friends_get(355070))
# pprint(groups_get(355070))
# json_to_file(groups_get(355070))
# print(groups_isMember('30936477', 355070))
# print(members_get_friends('30936477', 355070))
# print(members_get('30936477'))
# print(members_get('30936477'))

if __name__ == "__main__":
	print(groups_isMember('30936477', '35egrg5070'))
	pprint(groups_get(355070))

