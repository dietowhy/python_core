secret_number = 37
user_number = None
counter = 0
while user_number != secret_number:
    user_number = int(input("Enter number:"))
    counter += 1
    if user_number < secret_number:
        print("Введенное число меньше секретного")
    elif user_number > secret_number:
        print("Введенное число больше секретного")

print("Успешно!", "Число попыток:", counter)


