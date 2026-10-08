with open('numbers.txt') as file:
    numbers_list = []
    for line in file.readlines():
        number = int(line)
        numbers_list.append(number)

if len(numbers_list) < 3:
    print('Кол-во чисел в файле должно быть > 3!')
else:
    print('Первый элемент:', numbers_list[0], 'Второй элемент:', numbers_list[1], 'Последний элемент:',numbers_list[-1], 'Предпоследний элемент:', numbers_list[-2])