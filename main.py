import csv

print('Введите название файла для парсинга:')
name_of_the_file = input()

with open(f'./data_csv/{name_of_the_file}.csv', 'r', encoding='utf-8') as f_input:
    inc_col = [0, 2, 3]
    new_csv = []
    reader = csv.reader(f_input, delimiter=",")
    for row in reader:
        col = list(row[i] for i in inc_col)
        if col[1] == 'manager':
            new_csv.append(col)

names_csv = []
with open('./data_csv/names.csv', 'r', encoding='utf-8') as f_names:
    names = csv.reader(f_names)
    for row in names:
        names_csv.append(row)

names_csv.pop(0)

gb_csv = []
with open('./data_csv/good_bye.csv', 'r', encoding='utf-8') as f_gb:
    gb = csv.reader(f_gb)
    for row in gb:
        gb_csv.append(row)

greetings_csv = []
with open('./data_csv/greetings.csv', 'r', encoding='utf-8') as f_greetings:
    greetings = csv.reader(f_greetings)
    for row in greetings:
        greetings_csv.append(row)

repl = []
i = 0
while i != len(new_csv):
    repl.append([new_csv[i][0], new_csv[i][2]])
    i += 1

number_of_dialogs = int(new_csv[-1][0]) + 1
i = 0
greetings_csv.pop(0)
answer = ''
name_of_company = []
while i != number_of_dialogs:
    y = i
    for row in repl:
        if y == int(row[0]):
            for greeting in greetings_csv:
                if greeting[0].lower() in row[1].lower():
                    answer += f'Менеджер №{y + 1} поздоровался.\n'
                    print(f'Менеджер №{y + 1} поздоровался.')
                    print(f'Реплика: {row[1]}')
                    print("_" * 100)
            for name in names_csv:
                if f'меня зовут {name[0]}'.lower() in row[1].lower() or f'это {name[0]}'.lower() in row[1].lower() or \
                        f'меня {name[0]} зовут'.lower() in row[1].lower():
                    print(f'Менеджера №{y + 1} зовут {name[0]}.')
                    print(f'Реплика: {row[1]}')
                    print("_" * 100)
                    break
            for gb in gb_csv:
                if gb[0].lower() in row[1].lower():
                    answer += f'Менеджер №{y + 1} попрощался.\n'
                    print(f'Менеджер №{y + 1} попрощался.')
                    print(f'Реплика: {row[1]}')
                    print("_" * 100)
                    break
            if len(row[1][row[1].find('компания'):int(row[1].find('бизнес') + 6)]) > 2:
                name_of_company.append(f'Название компании №{y + 1}: ' \
                                       f'{row[1][row[1].find("компания"):int(row[1].find("бизнес") + 6)]}.')
    i += 1

i = 0
while i != number_of_dialogs:
    y = i
    if f'Менеджер №{y + 1} поздоровался.' not in answer:
        print(f'Менеджер №{y + 1} не поздоровался.')
    if f'Менеджер №{y + 1} попрощался.' not in answer:
        print(f'Менеджер №{y + 1} не попрощался.')
    i += 1

for n in name_of_company:
    print(n)
