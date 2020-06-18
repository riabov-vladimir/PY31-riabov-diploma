import json
from pprint import pprint


def json_to_file(script_result):
	"""Функция для сериализации json-данных в файл 'groups.json' """
	with open('groups.json', 'w', encoding='utf-8') as output_file:
		json.dump(script_result, output_file, ensure_ascii=False, indent=4)


def print_json_file(input_file='groups.json'):
	"""Функция для десериализации json файлов"""
	with open(input_file, encoding='utf-8') as file:
		reader = json.load(file)
		pprint(reader)
