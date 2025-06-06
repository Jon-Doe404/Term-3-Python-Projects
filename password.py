# Jon Joseph Catipon
# This function checks if a password is strong.
# A good password must have at least 8 characters, 
# include at least one uppercase letter, one lowercase letter, and one number.
# 4/4/2025
# 2024-140029

def check_password(pwd):
    if len(pwd) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        if has_upper and has_lower and has_digit:
            return True
    return False

password = input("Enter a password: ")
if check_password(password):
    print("Password is good.")
else:
    print("Password is not good.")
cool