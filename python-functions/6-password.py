def validate_password(password):
    if(len(password) > 8 and len(password) < 15):
        lowercase = False
        uppercase = False
        num = False
        special = False
        for char in password:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowercase = True
            if(char.isupper()):
                uppercase = True
            if(not char.isalnum()):
                special = True
        return lowercase and uppercase and num and special
    else:
        return False

