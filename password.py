user_name = input("enter user name: ")
password = input("enter your password: ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','&','%','(' ')','*','+','@']
has_letter = False
has_number = False
has_symbol = False
for i in password:
    if i in letters:
        has_letter = True
    elif i in numbers:
        has_number = True
    elif i in symbols:
        has_symbol = True
if has_number and has_symbol and has_letter:
    print("Your have a strong password")
elif (has_letter and has_number) or (has_letter and has_symbol):
    print("Your password is not much stronger")
else:
    print("Your password is weak ")
