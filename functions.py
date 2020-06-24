import json
from pprint import pprint
from requests_ import groups_is_member
import time


def json_to_file(script_result):
	"""Функция для сериализации json-данных в файл 'groups.json' """
	with open('groups.json', 'w', encoding='utf-8') as output_file:
		json.dump(script_result, output_file, ensure_ascii=False, indent=4)


def print_json_file(input_file='groups.json'):
	"""Функция для десериализации json файлов"""
	with open(input_file, encoding='utf-8') as file:
		reader = json.load(file)
		pprint(reader)


def sort_groups(groups, friends):

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

	groups_sorted = list(set(groups) - set(target_list))  # вычитаем получившийся список из списка всех групп
	# пользователя

	return groups_sorted
