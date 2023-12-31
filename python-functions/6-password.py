def validate_password(password):
    if(len(password) > 8):
        lowercase = False
        uppercase = False
        num = False
        space = True
        for char in password:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowercase = True
            if(char.isupper()):
                uppercase = True
            if(not char.isalnum()):
                space = False
        return lowercase and uppercase and num and space
    else:
        return False

