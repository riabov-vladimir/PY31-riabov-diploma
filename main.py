from requests_ import groups_get, groups_is_member, friends_get, get_int_id, groups_list_info
from pprint import pprint
from functions import json_to_file, print_json_file
import time

user_id = get_int_id('arbore')  # пользователь

groups = groups_get(user_id)  # все группы пользователя

friends = friends_get(user_id)  # все друзья пользователя

target_list = []

for group in groups:

	target = groups_is_member(group, friends)

	for user in target:
		if user['member'] == 1:
			target_list.append(group)
			break
	print('.')
	time.sleep(0.4)


groups = list(set(groups) - set(target_list))

print('Группы в которых состоит пользователь, но не состоят его друзья:\n' + str(groups))

groups_info = groups_list_info(target_list)

for group in groups_info:
	del group['is_closed']
	del group['photo_100']
	del group['photo_200']
	del group['photo_50']
	del group['screen_name']
	del group['type']

json_to_file(groups_info)
