test_results = str(input('Введите результаты тестов:'))
test_results_list = test_results.split()

def get_test_statistics(results):
    
    result_dict = {}
    list_count = len(results)
    pass_count = results.count("PASS")
    fail_count = results.count("FAIL")
    skip_count = results.count("SKIP")
    pass_percent = round((pass_count / list_count) * 100, 1)
    result_dict.update({'Всего тестов': list_count, 'PASS': pass_count, 'FAIL': fail_count, 'SKIP': skip_count, 'Успешно': pass_percent})
    
    return result_dict

status = get_test_statistics(test_results_list)

for key, value in status.items():
    print(f"{key}: {value}")