from requests_ import groups_get, groups_is_member, friends_get, get_int_id, groups_list_info
from pprint import pprint
from functions import json_to_file, print_json_file
import time
import datetime

user_input = input('Введите id пользователя или его screen_name')
if user_input.


user_id = get_int_id()  # пользователь по умолчанию arbore (функция принимает и screen name и user id)

groups = groups_get(user_id)  # все группы пользователя

friends = friends_get(user_id)  # все друзья пользователя

timer = str(datetime.timedelta(seconds=(len(groups) * 0.5)))  # вычисляю примерное время ожидания
# 0.4 сек задержка между запросами + 0.1 сек приерное время сопутствующих операций * кол-во запросов
print(f'Примерное время выполнение кода: {timer} \n Ожидайте...')

target_list = []  # сюда будем складывать группы в которых состоят друзья

for group in groups:  # пройдемся по списку групп

	target = groups_is_member(group, friends)  # для каждой группы отправим запрос на API VK, он вернёт нам список
	# словарей по вхождению каждого друга в эту группу

	for user in target:  # пройдемся циклом по этим словарям
		if user['member'] == 1:
			target_list.append(group)
			break  # если хотя бы один друг входит в эту группу, добавляем номер группы в список target_list
	print('.')  # показываем, что программа не зависла
	time.sleep(0.4)  # не даём циклу превысить кол-во обращений к API VK


groups = list(set(groups) - set(target_list))  # вычитаем получившийся список из списка всех групп пользователя

print('Группы в которых состоит пользователь, но не состоят его друзья:\n' + str(groups) + '\n')  # сообщение в консоль

groups_info = groups_list_info(groups)  # запрашиваем у API VK информацию о группах из получившегося списка

for group in groups_info:  # из информации о группах убираем всё лишнее
	del group['is_closed']
	del group['photo_100']
	del group['photo_200']
	del group['photo_50']
	del group['screen_name']
	del group['type']

json_to_file(groups_info)  # сериализуем данные в файл .json формата
print('Для вывода в консоль содержимого файла "groups.json" нажмите Enter \n\nДля окончания работы '
				'программы введите любой символ и нажмите Enter\n>>>')
user_input = input()

if user_input == '':
	print_json_file()
else:
	print('До свидания!')
	pass

