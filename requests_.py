import requests
from pprint import pprint
import time

access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

base_url = 'https://api.vk.com/method/'

base_params = {'access_token': access_token, 'v': 5.107}

def user_id_str_to_int(user_id: str) -> int:
	"""
	функция принимающая screen_name и возвращающая числовой id пользовтаеля
	"""

	request_url = base_url + 'users.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_ids': user_id,
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response'][0]['id']
	return json_

def check_user(user_id: int):
	"""deactivated
	string	поле возвращается, если страница пользователя удалена или заблокирована, содержит значение deleted или banned. В этом случае опциональные поля не возвращаются.
	is_closed
	boolean	скрыт ли профиль пользователя настройками приватности."""
	request_url = base_url + 'users.get'
	params = base_params.copy()
	params['user_id'] = user_id
	response = requests.get(request_url, params=params)
	json_ = response.json()

	if json_['response'][0].get('is_closed') == True:
		print('Пользователь ограничил доступ к своей странице')
		# exit()
	elif json_['response'][0].get('is_closed') == False:
		print('ok')
	elif json_['response'][0].get('deactivated') == 'deleted':
		print('Пользователь удалён или заблокирован')
	# 	exit()
	elif json_['response'][0].get('deactivated') == 'banned':
		print('Пользователь заблокирован')


def friends_get(user_id: int) -> list:

	"""функция возвращающая список друзей пользовтаеля"""

	request_url = base_url + 'friends.get'
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

	request_url = base_url + 'groups.get'
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

	request_url = base_url + 'groups.isMember'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_id': group_id,
		'user_ids': str(user_ids)[1:-1:]
	}

	response = requests.get(request_url, params=params)

	json_ = response.json()['response']

	return json_


def groups_list_info(groups_list: list):

	request_url = base_url + 'groups.getById'

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



	pprint(check_user(user_id_str_to_int('anyagrapes')))

	pprint(check_user(372957))
	time.sleep(0.2)
	pprint(check_user(143302813))

	check_user(171691064)

	pprint(groups_get(171691064))

