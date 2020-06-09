def write_to_file(script_result): # запись текста в файл, переделать под json
	with open('groups.json', 'w', encoding='utf-8') as output_file:
		output_file.write(script_result)

# Сериализация В файл: json.dump() Печать не-ascii символов, отступыensure_ascii=False, indent=2

# Виталий, а зачем тебе все группы всех друзей парсить?
# Есть же в ВК готовый метод, который сразу показывает
# какие в у тебя есть общие группы с друзьями. У меня все улеглось в 2 запроса...

if __name__ == '__main__':
	output = 'vwpиуиуки уки укук рv owenv owenv oien ow'
	write_to_file(output)