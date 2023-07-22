def validate_password(password):
    if(len(password) > 8 and len(password) < 15):
        lowercase = False
        uppercase = False
        number = False
        special = False
        for char in password:
            if(char.isdigit()):
                number = True
            if(char.islower()):
                lowercase = True
            if(char.isupper()):
                uppercase = True
            if(not char.isalnumber()):
                special = True
        return lowercase and uppercase and number and special
    else:
        return False

