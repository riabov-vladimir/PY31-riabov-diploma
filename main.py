from requests_ import groups_get, groups_is_member, friends_get, get_int_id, groups_list_info
from pprint import pprint
from functions import json_to_file, print_json_file
import time

user_id = get_int_id(171691064)  # пользователь с 3 друзьями и ~20 группами

groups = groups_get(user_id)  # все группы пользователя
print(groups)
friends = friends_get(user_id)  # все друзья пользователя

target_list = groups.copy()
print('target list: ' + str(target_list))
for group in groups:
	print(group)
	try:
		target = groups_is_member(group, friends)
	except Exception as e:
		print(e)
	for user in target:
		if user['member'] == 1:
			target_list.remove(group)
	print('.')
	time.sleep(0.4)

print('Группы в которых состоит пользователь, но не состоят его друзья:\n' + str(target_list))

groups_info = groups_list_info(target_list)

for group in groups_info:
	del group['is_closed']
	del group['photo_100']
	del group['photo_200']
	del group['photo_50']
	del group['screen_name']
	del group['type']

json_to_file(groups_info)
