import json
from functools import reduce

input_file = "tests_results.json"
output_file = "test_report.json"

statuses = ("PASS", "FAIL", "SKIP")
fields = ("name", "status", "duration")

def load_results(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Файл '{path}' не найден: {e}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Не удалось прочитать JSON из '{path}': {e}") from e
    except OSError as e:
        raise RuntimeError(f"Ошибка ввода-вывода при чтении '{path}': {e}") from e

    if not isinstance(data, list):
        raise RuntimeError("Ожидался список тестов в корне JSON-файла.")

    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise RuntimeError(f"Элемент #{i} не является объектом.")
        for field in fields:
            if field not in item:
                raise RuntimeError(f"В элементе #{i} отсутствует поле '{field}'.")
        if item["status"] not in statuses:
            raise RuntimeError(
                f"В элементе #{i} недопустимый статус: {item['status']}."
            )
        if not isinstance(item["duration"], (int, float)) or item["duration"] < 0:
            raise RuntimeError(
                f"В элементе #{i} некорректное время выполнения: {item['duration']}."
            )

    return data

def build_report(tests):
    failed_tests = list(
        map(lambda t: t["name"], filter(lambda t: t["status"] == "FAIL", tests))
    )

    passed_tests = [t["name"] for t in tests if t["status"] == "PASS"]

    skipped_tests = [t["name"] for t in tests if t["status"] == "SKIP"]

    total_duration = reduce(lambda acc, t: acc + t["duration"], tests, 0.0)

    longest_test = reduce(
        lambda a, b: a if a["duration"] >= b["duration"] else b,
        tests,
    ) if tests else None

    counts = {
        status: len(list(filter(lambda t, s=status: t["status"] == s, tests)))
        for status in statuses
    }

    report = {
        "total_tests": len(tests),
        "passed": counts["PASS"],
        "failed": counts["FAIL"],
        "skipped": counts["SKIP"],
        "failed_tests": failed_tests,
        "passed_tests": passed_tests,
        "skipped_tests": skipped_tests,
        "longest_test": (
            {"name": longest_test["name"], "duration": longest_test["duration"]}
            if longest_test else None
        ),
        "total_duration": round(total_duration, 2),
    }
    return report

def save_report(report, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
    except OSError as e:
        raise RuntimeError(f"Не удалось сохранить отчёт в '{path}': {e}") from e

def main():
    try:
        tests = load_results(input_file)
    except RuntimeError as e:
        print(f"Ошибка загрузки данных: {e}")
        return

    report = build_report(tests)

    try:
        save_report(report, output_file)
    except RuntimeError as e:
        print(f"Ошибка сохранения отчёта: {e}")
        return

    print(f"Всего тестов:{report['total_tests']}")
    print(f"PASS:{report['passed']}")
    print(f"FAIL:{report['failed']}")
    print(f"SKIP:{report['skipped']}")
    print(f"Упавшие тесты ({report['failed']}): {report['failed_tests']}")
    print(f"Успешные тесты ({report['passed']}): {report['passed_tests']}")
    print(f"Пропущенные тесты ({report['skipped']}): {report['skipped_tests']}")
    if report["longest_test"]:
        lt = report["longest_test"]
        print(f"Самый длительный тест: {lt['name']} ({lt['duration']} с)")
    print(f"Суммарное время выполнения: {report['total_duration']} с")

if __name__ == "__main__":
    main()