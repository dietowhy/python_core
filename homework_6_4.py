from functools import wraps

def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt}")
                result = func(*args, **kwargs)
                if result is True:
                    return result
            return result
        return wrapper
    return decorator

attempts = 0

@retry(5)
def unstable_test(name, success_on=3):
    global attempts
    attempts += 1
    print(f"Выполнение теста {name}, попытка {attempts}")
    return attempts >= success_on

print("Итог:", unstable_test("login", success_on=3))