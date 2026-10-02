def run_test_with_retries(retries, timeout):
    if not isinstance(retries, int) or isinstance(retries, bool):
        raise ValueError(
            f"Количество повторных запусков должно быть целым числом, получено:{retries!r}"
        )
    if not (0 <= retries <= 5):
        raise ValueError(
            f"Количество повторных запусков должно быть в диапазоне от 0 до 5, получено:{retries}"
        )

    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool):
        raise ValueError(
            f"Таймаут должен быть числом, получено:{timeout!r}"
        )
    if timeout <= 0:
        raise ValueError(
            f"Таймаут должен быть положительным числом, получено:{timeout}"
        )

    return {"retries": retries, "timeout": timeout}

test_cases = [
    (3, 30),
    (2, -5),
    (10, 15),
]

for retries, timeout in test_cases:
    print(f"Проверка: retries={retries}, timeout={timeout}")
    try:
        config = run_test_with_retries(retries, timeout)
    except ValueError as e:
        print(f"Ошибка: {e}")
    else:
        print(f"Успешно настроено: {config}")
    print()