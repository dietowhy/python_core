class InvalidTestStatusError(Exception):
    pass


statuses = ("PASS", "FAIL", "SKIP")


def check_test_status(status):
    if status not in statuses:
        raise InvalidTestStatusError(
            f"Недопустимый статус теста: {status}. "
            f"Допустимые значения: {', '.join(statuses)}."
        )
    return status

test_cases = ["PASS", "FAIL", "SKIP", "ERROR", "pass", "", None, 42]

for status in test_cases:
    print(f"Проверка статуса:{status}")
    try:
        result = check_test_status(status)
    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")
    else:
        print(f"Статус принят: {result}")
    print()