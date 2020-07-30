def has_digit(password):
    return any(map(str.isdigit, password))

def has_upper_latter(password):
    return any(map(str.isupper, password))

def has_lower_latter(password):
    return any(map(str.islower, password))

def has_special_character(password):
    allowed_special_characters = ['!', '/', "#"]
    for i in allowed_special_characters:
        if i in password:
            return True
    return False

def not_has_special_character(password):
    not_allowed_characters = ['@', '\'', "{", "}"]
    for i in not_allowed_characters:
        if i in password:
            return True
    return False

def check_password(password):
    is_allowed_password = True
    resutl = ''
    if len(password) <6:
        resutl += '*lungimea trebuie sa fie minim 6 caractere\n'
        is_allowed_password = False

    if not has_digit(password):
        resutl += '*parola trebuie sa contina cel putin 1 cifra\n'
        is_allowed_password = False

    if not has_lower_latter(password):
        resutl += '*parola trebuie sa contina cel putin 1 litera mica [a-z]\n'
        is_allowed_password = False

    if not has_upper_latter(password):
        resutl += '*parola trebuie sa contina cel putin 1 litera mare [A-Z]'
        is_allowed_password = False

    if not has_special_character(password):
        print('*parola trebuie sa contina cel putin 1 caracter special [!, /, #]')
        is_allowed_password = False
    
    if not_has_special_character(password):
        print('*parola nu trebuie sa contina [@, \', {, }]')
        is_allowed_password = False

    if not is_allowed_password:
        print(resutl)

    return is_allowed_password

is_done = False
while not is_done:
    a = str(input('insert password: '))
    is_done = check_password(a)