password = input("Enter your password: ")

length_true = len(password) > 6
number_true = False
special_true = False
upper_true = False
lower_true = False

special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

for char in password:
    if char >= '0' and char <= '9':
        number_true = True
    elif char in special_chars:
        special_true = True
    elif char >= 'A' and char <= 'Z':
        upper_true = True
    elif char >= 'a' and char <= 'z':
        lower_true = True

if length_true and number_true and special_true and upper_true and lower_true:
    print("Password is valid")
else:
    print("Password is invalid")
    if not length_true:
        print("Password must be more than 6 characters")
    if not number_true:
        print("Password must have a digit")
    if not special_true:
        print("Password must have a special character")
    if not upper_true:
        print("Password must have an uppercase letter")
    if not lower_true:
        print("Password must have a lowercase letter")
