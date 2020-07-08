from requests_ import groups_get, friends_get, groups_list_info, check_user
from functions import json_to_file, print_json_file, sort_groups
import datetime

"""
Ввод данных (идентификатор пользователя) осуществляется через консоль. Аргументом может быть как id так и screen_name.
Идентификаторы, которые я использовал для проверки программы:
372957 - Пользователь удалён
anyagrapes - Пользователь заблокирован
eshmargunov - открытый профиль, программа отрабатывает полностью
arbore - закрытый профиль
"""

if __name__ == '__main__':

	print('Введите id пользователя или его screen name')
	user_input = input('>>>').lower()

	user_id = check_user(user_input)
	# проверяем доступ к данным пользователя (функция принимает и screen name и user id)

	groups = groups_get(user_id)  # все группы пользователя

	friends = friends_get(user_id)  # все друзья пользователя

	timer = str(datetime.timedelta(seconds=(len(groups) * 0.5)))
	"""вычисляю примерное время ожидания 0.4 сек задержка между запросами + 0.1 сек примерное время сопутствующих 
	операций * кол-во запросов"""

	print(f'Примерное время выполнение кода: {timer} \n Ожидайте...')

	sorted_groups = sort_groups(groups, friends)

	print('Группы в которых состоит пользователь, но не состоят его друзья:\n' + str(sorted_groups) + '\n')

	groups_info = groups_list_info(sorted_groups)  # запрашиваем у API VK информацию о группах из получившегося списка

	json_to_file(groups_info)  # сериализуем данные в файл .json формата
	print('Для вывода в консоль содержимого файла "groups.json" нажмите Enter \n\nДля окончания работы '
					'программы введите любой символ и нажмите Enter\n>>>')
	user_input = input()

	if user_input == '':
		print_json_file()
	else:
		print('До свидания!')
