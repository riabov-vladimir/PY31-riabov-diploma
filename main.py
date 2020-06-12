from requests_ import groups_get, groups_isMember, friends_get, user_id_str_to_int
import time
from functions import group_append

access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

user_id = user_id_str_to_int('arbore') # (eshmargunov) и id (171691064)

groups = groups_get(user_id)
group_append('Ksenia groups :' + str(groups))

friends = friends_get(user_id)
group_append('Ksenia friends :' + str(friends))

target = groups.copy()

for group in groups:
	print('iterating for group ' + str(group))
	for friend in friends:
		print(str(friend) + ' + ' + str(group))
		time.sleep(0.34)
		if groups_isMember(str(group), friend) == 1:
			print('found match          <---------------------- ')
			target.remove(group)
			break
	else:
		print('no match')



print('target group = ' + str(target))

group_append(groups_get(user_id))