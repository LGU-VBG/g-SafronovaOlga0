import re

def passwordcheck (paswrd):
    if len(paswrd) < 8:
        return("Your password is short")
    if re.search(r"[a-z]+[A-Z]+[0-9]+[!?@#$%^&*()_-|\/><,.:;~{}\"\']", paswrd):
        return ("Password accepted")
    else:
        return ("Password entered incorectly.\nAdd lower,upper case letters, numbers or special ones")

password_user= input("Enter your password: ")

print(passwordcheck(password_user))

