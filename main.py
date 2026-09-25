import test_data

number_of_users = int(input('Введите кол-во тестовых пользователей:'))
users_list = []
active_count = 0
blocked_count = 0
inactive_count = 0

for i in range(number_of_users):
    users_list.append(test_data.generate_user(number_of_users))

for user in users_list:
    print(f"Логин: {user['login']} | Возраст: {user['age']} | Статус: {user['status']}")

for user in users_list:
    if user['status'] == "ACTIVE":
        active_count += 1
    elif user['status'] == "BLOCKED":
        blocked_count += 1
    elif user['status'] == "INACTIVE":
        inactive_count += 1

print(f"ACTIVE   - {active_count}")
print(f"BLOCKED  - {blocked_count}")
print(f"INACTIVE - {inactive_count}")