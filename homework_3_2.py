test_cases = [ "Login", "Registration", "Checkout", "Logout" ]
statuses = [ "PASS", "FAIL", "PASS", "SKIP" ]

def print_report(test_cases, statuses):
    for test, status in zip(test_cases, statuses):
        print(f"{test} - {status}")

print_report(test_cases, statuses)

fail_count = statuses.count("FAIL")

if fail_count > 0:
    print("Запуск тестов прошел не успешно!")
else:
    print("Запуск тестов прошел успешно!")
