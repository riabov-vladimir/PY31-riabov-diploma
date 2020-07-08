import requests


def _request(req_method, **params):
	URL = 'https://api.vk.com/method/' + req_method

	data = {
		'access_token': '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008',
		'v': 5.107
	}
	data.update(params)
	response = requests.post(URL, data=data)

	if response.status_code != 200:
		return

	_json = response.json()

	if 'error' in _json:
		print(f'''Ошибка: {_json.get('error')['error_msg']}''')
		return

	return _json.get('response')


def request(req_method, **params):
	answer = _request(req_method, **params)

	if not answer:
		exit(0)
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

	response = request('users.get', user_ids=str(user_input).join(', '))

	if response[0].get('is_closed'):
		print('Пользователь ограничил доступ к своей странице.\n')
		exit()
	elif response[0].get('deactivated') == 'deleted':
		print('Пользователь удалён.\n')
		exit()
	elif response[0].get('deactivated') == 'banned':
		print('Пользователь заблокирован.\n')
		exit()
	elif not response[0].get('is_closed'):
		return response[0]['id']  # числовой идентификатор


def friends_get(user_id: int) -> list:

	"""
	Функция возвращающая список друзей пользовтаеля.
	*Ограничил кол-во возвращаемых идентификаторов до 500, для того, чтобы в дальнейшем уложиться
	в лимит аргументов user_ids метода 'groups.isMember'
	:param user_id: int
	:return: list of int
	"""

	response = request('friends.get', count=500, user_id=user_id)

	return response['items']


def groups_get(user_id: int) -> list:

	"""Функция возвразающая список групп, в которых состоит указанный пользователь"""

	response = request('groups.get', user_id=user_id)

	return response['items']


def groups_is_member(group_id: str, user_ids: list) -> list:

	"""
	Функция принимающая в качестве аргумента список идентификаторов пользователей и идентификатор группы,
	а возвращающая список из словарей, содержащих подробную информацию о принадлежности каждого из пользователей к
	указанной группе

	:param group_id:
	:param user_ids:
	:return: list of dicts
	"""

	respopnse = request('groups.isMember', user_ids=str(user_ids).join(', '), group_id=group_id)

	return respopnse


def groups_list_info(groups_list: list):
	"""
	Функция принимающая в качестве аргумента список идентификаторов групп и возвращающая список из словарей,
	содержащих подробную информацию о каждой группе

	:param groups_list: list of int
	:return: list of dicts
	"""

	groups_raw = request('groups.getById', fields='members_count', group_ids=str(groups_list).join(', '))

	groups_filtered = []

	excluded_fields = ['is_closed', 'photo_100', 'photo_200', 'photo_50', 'screen_name', 'type']

	for group in groups_raw:
		filtered_group = {key: value for (key, value) in group.items() if key not in excluded_fields}
		groups_filtered.append(filtered_group)

	return groups_filtered


if __name__ == '__main__':
	user_input = 171691064
	user_ids = [4929, 7858, 11952, 48807, 58439, 71491, 75458, 78540, 105932, 143611, 144253]
	# response = request('users.get', user_ids=str(user_input).join(', '))
	# print(response)
	print(groups_is_member('171691064', user_ids))
