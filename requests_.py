import requests
from pprint import pprint
import time

access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

base_url = 'https://api.vk.com/method/'
base_params = {'access_token': access_token, 'v': 5.107}


def json_check(response):
	"""Проверка ответа API VK на наличие ключа 'response', который присутствует в верно выполненных запросах"""
	try:
		answer = response.json()['response']
	except KeyError as e:
		print('Ошибка: ' + str(e))
		exit()
	else:
		return answer


def check_user(user_input) -> int:
	"""
	Наверное, не очень грамотно делать такую нагроможденную функцию, но я всё же решил совместить запрос
	на проверку состояния страницы пользователя (удалена, заблокирована, отсутствует) и приведение идентификатора
	к численному виду, т.к. очень удобно делать рекурсию на повторный запрос консольного ввода.
	*Запрос users.get, как я выяснил буквально вчера, принимает как str, так и int -- очень удобно!
	:return: user_id (integer)
	"""

	request_url = base_url + 'users.get'
	params = base_params.copy()
	params['user_ids'] = user_input
	response = requests.get(request_url, params=params)

	if json_check(response)[0].get('is_closed'):
		print('Пользователь ограничил доступ к своей странице.\n')
		exit()
	elif json_check(response)[0].get('deactivated') == 'deleted':
		print('Пользователь удалён.\n')
		exit()
	elif json_check(response)[0].get('deactivated') == 'banned':
		print('Пользователь заблокирован.\n')
		exit()
	elif not json_check(response)[0].get('is_closed'):
		return json_check(response)[0]['id']  # числовой идентификатор


def friends_get(user_id: int) -> list:

	"""
	Функция возвращающая список друзей пользовтаеля.
	*Ограничил кол-во возвращаемых идентификаторов до 500, для того, чтобы в дальнейшем уложиться
	в лимит аргументов user_ids метода 'groups.isMember'
	:param user_id: int
	:return: list of int
	"""

	request_url = base_url + 'friends.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		'count': 500,
	}

	response = requests.get(request_url, params=params)

	return json_check(response)['items']


def groups_get(user_id: int) -> list:

	"""Функция возвразающая список групп, в которых состоит указанный пользователь"""

	request_url = base_url + 'groups.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		'count': 500
	}

	response = requests.get(request_url, params=params)

	return json_check(response)['items']


def groups_is_member(group_id: str, user_ids: list) -> list:

	"""
	Функция принимающая в качестве аргумента список идентификаторов пользователей и идентификатор группы,
	а возвращающая список из словарей, содержащих подробную информацию о принадлежности каждого из пользователей к
	указанной группе

	:param group_id:
	:param user_ids:
	:return: list of dicts
	"""

	request_url = base_url + 'groups.isMember'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_id': group_id,
		'user_ids': str(user_ids)[1:-1:]
	}

	response = requests.get(request_url, params=params)

	return json_check(response)


def groups_list_info(groups_list: list):
	"""
	Функция принимающая в качестве аргумента список идентификаторов групп и возвращающая список из словарей,
	содержащих подробную информацию о каждой группе

	:param groups_list: list of int
	:return: list of dicts
	"""

	request_url = base_url + 'groups.getById'

	params = {
		'access_token': access_token,
		'v': 5.107,
		'group_ids': str(groups_list)[1:-1:],
		'fields': 'members_count'
	}
	response = requests.get(request_url, params=params)

	groups_raw = json_check(response)

	groups_filtered = []

	excluded_fields = ['is_closed', 'photo_100', 'photo_200', 'photo_50', 'screen_name', 'type']

	for group in groups_raw:
		filtered_group = {key: value for (key, value) in group.items() if key not in excluded_fields}
		groups_filtered.append(filtered_group)

	return groups_filtered


if __name__ == '__main__':
	print(friends_get('wefefwf'))

