import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['1','@','#','$','%','&','*','(',')','+']
print("welcome to password generator")
no_of_letters = int(input("enter the no. of letters u want to include in your password:"))
no_of_numbers = int(input("enter the no. of numbers u want to include in your password:"))
no_of_symbols = int(input("enter the no. of symbols u want to include in your password:"))
password_list = []
for i in range (1 , no_of_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char
for i in range (1 , no_of_numbers + 1):
    randam_num = str(random.choice(numbers))
    password_list += randam_num
for i in range (1 , no_of_symbols + 1):
    random_sym = random.choice(symbols)
    password_list += random_sym
total_char = no_of_letters + no_of_numbers + no_of_symbols
random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print(f"your password can be {password}")