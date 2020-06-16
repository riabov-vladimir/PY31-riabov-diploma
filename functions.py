import json
from pprint import pprint
import time
import os


def json_to_file(script_result):
	"""функция записывающая данные в файл 'groups.json' """
	with open('groups.json', 'w', encoding='utf-8') as output_file:
		json.dump(script_result, output_file, ensure_ascii=False, indent=4)


def group_append(text):
	"""
	Функция для логирования моих расчётов
	:param text:
	:return:
	"""
	with open('output_file.txt', 'a', encoding='utf-8') as output_file:
		output_file.write(os.linesep)
		# output_file.write(str(datetime.datetime.utcnow()))
		output_file.write(str(text))


def print_json_file(input_file):
	"""функция для десериализации json файлов, использую для проверки записаных файлов"""
	with open(input_file, encoding='utf-8') as file:
		reader = json.load(file)
		pprint(reader)





if __name__ == '__main__':
	print(get_int_id('eshmargunov'))
