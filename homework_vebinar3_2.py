#Задание 2
right_password = "Python123"
for i in range(3):
    user_password = input('Enter your password:')
    if user_password == right_password:
        print("Logged in successfully.")
        break
    else:
        print("Access blocked!")