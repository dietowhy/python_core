from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест {func.__name__} завершён. Результат: {result}")
        return result
    return wrapper

@log_test
def test_sum(a, b, expected=5):
    return a + b == expected

print(test_sum(2, 3))
print(test_sum(1, 2, expected=5))
print(test_sum.__name__)