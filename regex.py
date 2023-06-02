import re

def passwd_validation(passwd):
    pattern="^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$"
    return bool(re.match(pattern,passwd))

print(passwd_validation("Mohammad"))
print(passwd_validation("Mohammad21"))
