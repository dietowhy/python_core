import random

characters_list = [ 

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'

]

status_pull = [ "ACTIVE", "BLOCKED", "INACTIVE" ]

def generate_login(char_list, lenght):
    login = "".join(random.choices(char_list, k = lenght))
    return login

def generate_age():
    age = random.randint(10, 80)
    return age

def generate_status(status_pull):
    status = random.choice(status_pull)
    return status


def generate_user(number_of_users):
    user_dict = {
        'login': generate_login(characters_list, 10),
        'age': generate_age(),
        'status': generate_status(status_pull)
    }
    return user_dict