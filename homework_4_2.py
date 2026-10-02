with open('numbers.txt') as file:
    numbers_list = []
    for line in file.readlines():
        number = int(line)
        numbers_list.append(number)

for number in numbers_list:
    if number % 2 == 0:
        with open('even_number.txt', 'a') as even_file:
            even_file.writelines(f"{str(number)}\n")
    else:
        with open('odd_number.txt', 'a') as odd_file:
            odd_file.writelines(f"{str(number)}\n")