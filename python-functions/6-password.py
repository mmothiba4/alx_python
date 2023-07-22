def validate_password(password):
    if(len(password) > 8):
        lowerCase = False
        upperCase = False
        num = False
        special = False
        for char in password:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowerCase = True
            if(char.isupper()):
                upperCase = True
            if(not char.isalnum()):
                special = True
        return lowerCase and upperCase and num and special
    else:
        return False

