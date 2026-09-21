#Задание 5
tests_numbers = int(input("Введите число тестов: "))
test_arr = list(range(tests_numbers))
result_arr = []

for i in test_arr:
    test_result = str(input("Введите результат каждого теста (PASS, FAIL или SKIP): "))
    if test_result == "PASS" or test_result == "FAIL" or test_result == "SKIP":
        result_arr.append(test_result)
    else:
        continue

pass_count = result_arr.count("PASS")
fail_count = result_arr.count("FAIL")
skip_count = result_arr.count("SKIP")

print("Успешных тестов:", pass_count)
print("Проваленных тестов:", fail_count)
print("Пропущенных тестов:", skip_count)

if fail_count > 0:
    print("Не все тесты прошли!")
elif fail_count == 0:
    print("Все тесты прошли успешно!")
    
