#Задание 3
user_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in user_numbers:
    if i == 5 or i == 10 or i == 15:
        continue
    elif i == 18:
        break
    else:
        print("Для пользователя", i, "Тест запущен")