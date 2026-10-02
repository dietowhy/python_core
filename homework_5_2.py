import json

fildes = ("login", "password", "expected_result")
file_path = "tests_users.json"

def load_test_users(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Ошибка: файл '{path}' не найден. ({e})")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка: не удалось прочитать JSON из файла '{path}'. ({e})")
        return None
    except OSError as e:
        print(f"Ошибка ввода-вывода при работе с файлом '{path}'. ({e})")
        return None

    if not isinstance(data, list):
        print("Ошибка: ожидался список пользователей в JSON-файле.")
        return None

    return data


def print_user(index, user):
    try:
        if not isinstance(user, dict):
            raise TypeError(f"элемент #{index} не является объектом (dict)")

        for field in fildes:
            if field not in user:
                raise KeyError(f"у пользователя #{index} отсутствует поле '{field}'")

        print(f"Пользователь #{index}")
        print(f"Логин:{user['login']}")
        print(f"Пароль:{user['password']}")
        print(f"Ожидаемый итог:{user['expected_result']}")
    except KeyError as e:
        print(f"Пропуск: {e}")
    except TypeError as e:
        print(f"Пропуск: {e}")
    finally:
        print()


def main():
    users = load_test_users(file_path)
    if users is None:
        return

    print(f"Загружено записей: {len(users)}\n")
    for i, user in enumerate(users, start=1):
        print_user(i, user)


if __name__ == "__main__":
    main()