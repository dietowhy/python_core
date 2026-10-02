with open('numbers1.txt', 'r') as file:
    numbers_list = []
    for line in file:
        number = float(line)
        numbers_list.append(number)

with open('numbers1.txt', 'w') as file:
    for number in numbers_list:
        number_square = pow(number, 2)
        file.write(f"{number_square}\n")