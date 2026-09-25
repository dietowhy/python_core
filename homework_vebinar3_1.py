# Задание 1
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("BugTest")
    elif i % 3 == 0:
        print("Bug")
    elif i % 5 == 0:
        print("Test")
    else:
        print(i)

