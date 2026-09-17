# Задание 6
school = {
    "1а": 20,
    "1б": 22,
    "2б": 18,
    "6а": 25,
    "7в": 23,
    "8а": 24,
    "8б": 26,
    "9а": 27,
    "9б": 28,
    "10а": 29,
    "10б": 30,
}

print(school)

# Задание 7
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_element = list[1]
print(second_element)

# Задание 8
string1 = "dog"
string2 = "doggy"
result = string1 in string2
print(result)

# Задание 9
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3]) 

# Задание 10
array = [1, 5, 2, 9, 2, 9, 1]
for i in array:
    result = array.count(i)
    if result == 1:
        print(i)
