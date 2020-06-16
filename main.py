from requests_ import groups_get, groups_isMember, friends_get, user_id_str_to_int
import time


user_id = user_id_str_to_int('arbore') # пользователь с 3 друзьями и ~20 группами

groups = groups_get(user_id)  # все группы пользователя
group_append('Ksenia groups :' + str(groups))

friends = friends_get(user_id) # все друзья пользователя
group_append('Ksenia friends :' + str(friends))

target = groups.copy()
"""список всех групп пользователя из которых в цикле будет удаляться каждая группа
в которой состоит хотя бы один друг пользователя"""

for group in groups:
	print('iterating for group ' + str(group))
	for friend in friends:
		print(str(friend) + ' -> ' + str(group))
		time.sleep(0.4)
		if groups_isMember(str(group), friend) == 1:
			print('пользователь являяется участником группы, группа исключена из списка <---------------------- ')
			target.remove(group)
			break
	else:
		print('no match')


print('Группы в которых состоит пользователь, но не состоят его друзья:\n' + str(target))

group_append(groups_get(user_id))  # сохраняю на всякий случай резултат