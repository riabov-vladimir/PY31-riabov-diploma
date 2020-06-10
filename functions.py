import json
from pprint import pprint
import time
from requests_ import user_id_from_str


def json_to_file(script_result):
	"""функция записывающая данные в файл 'groups.json' """
	with open('groups.json', 'w', encoding='utf-8') as output_file:
		json.dump(script_result, output_file, ensure_ascii=False, indent=4)


def print_json_file(input_file):
	"""функция для десериализации json файлов, использую для проверки записаных файлов"""
	with open(input_file, encoding='utf-8') as file:
		reader = json.load(file)
		pprint(reader)


def get_int_id(user_id):
	"""

	!!!!!!!!!!!!      ВОПРОС №3        !!!!!!!!!!!!!!

	"""
	if type(user_id) == int:
		return user_id
	elif type(user_id) == str:
		return user_id_from_str(user_id)


if __name__ == '__main__':
	print(get_int_id('eshmargunov'))
