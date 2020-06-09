import requests

from pprint import pprint

access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008' # scope_friends


def friends_get(user_id: int or str) -> list:
	request_url = 'https://api.vk.com/method/friends.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		# 'count': 10,
		# 'order': 'name'
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_

def groups_get(user_id: int or str) -> list:
	request_url = 'https://api.vk.com/method/groups.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		# 'count': 10,
		# 'order': 'name'
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_

# pprint(friends_get(355070))


if __name__ == "__main__":
	pprint(groups_get(355070))
