float_number1 = -1.6
int_number = int(float_number1)
print(int_number)

float_number2 = 2.99
int_number2 = int(float_number2)
print(int_number2)

site_string = "www.my_site.com#about"
site_string = site_string.replace("#", "/")
print(site_string)

word = "stroka"
word = word.rstrip("a")
word = word + "ing"
print(word)

name_string = "Ivanou Ivan"
name_string = name_string.split()
name_string.reverse()
name_string = " ".join(name_string)
print(name_string)

some_string = "  some string  "
some_string = some_string.strip()
print(some_string)