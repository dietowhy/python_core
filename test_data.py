import random

characters_list = [ 

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'

]

status_pull = [ "ACTIVE", "BLOCKED", "INACTIVE" ]

def generate_login(lenght):
    login = "".join(random.choices(characters_list, k = lenght))
    return login

def generate_age():
    age = random.randint(10, 80)
    return age

def generate_status():
    status = random.choice(status_pull)
    return status


def generate_user():
    user_dict = {
        'login': generate_login(10),
        'age': generate_age(),
        'status': generate_status()
    }
    return user_dict