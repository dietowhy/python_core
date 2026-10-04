from functools import reduce
from collections import Counter

tests = [
    {"name": "test_login", "status": "PASS", "duration": 1.2},
    {"name": "test_logout", "status": "FAIL", "duration": 0.8},
    {"name": "test_payment", "status": "SKIP", "duration": 0.0},
    {"name": "test_profile", "status": "PASS", "duration": 2.1},
    {"name": "test_cart", "status": "FAIL", "duration": 1.5},
]

failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))

failed_names = list(map(lambda t: t["name"], failed_tests))

total_time = reduce(lambda acc, t: acc + t["duration"], tests, 0)

passed_names = [t["name"] for t in tests if t["status"] == "PASS"]

status_counts = Counter(t["status"] for t in tests)
for status in ("PASS", "FAIL", "SKIP"):
    status_counts.setdefault(status, 0)

print("Количество тестов по статусам:")
for status, count in status_counts.items():
    print(f"{status}: {count}")

print("Список упавших тестов:")
print(failed_names)

print("Список успешно пройденных тестов:")
print(passed_names)

print(f"Общее время выполнения всех тестов: {total_time:.2f}")