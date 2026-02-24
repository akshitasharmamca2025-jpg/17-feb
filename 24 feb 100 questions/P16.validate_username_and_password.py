import re

def validate_username(username):
    # Username: letters and numbers, 5-15 chars
    if re.fullmatch(r'[A-Za-z0-9]{5,15}', username):
        return True
    return False

def validate_password(password):
    # Password rules: min 8 chars, at least one upper, one lower, one digit, one special char
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Read input
username = input("Enter username: ")
password = input("Enter password: ")

# Validation
if validate_username(username):
    print("Username is valid")
else:
    print("Invalid username")

if validate_password(password):
    print("Password is valid")
else:
    print("Invalid password")

#------------------------------------------

#input: Input:
#Enter username: user123
#Enter password: Password@1

#Output:
#Username is valid
#Password is valid