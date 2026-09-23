import random 

tests = [ "test_login", "test_logout", "test_registration", "test_profile", "test_payment", "test_search"]
results_pull = [ "PASS", "FAIL", "SKIP" ]

while True: 
    tests_count = int(input("Введите кол-во тестов:"))
    if tests_count > len(tests):
        print("Вы ввели число, которое бельше общего числа тестов!")
        continue
    else:
        tests_result = []
        random_tests = random.sample(tests, tests_count)
        for test in random_tests:
            random_status = random.choice(results_pull)
            tests_result.append(f"{test} - {random_status}")
    break

for results in tests_result:
    print(results)


