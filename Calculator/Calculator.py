from calculator_art import logo

print(logo)
#for Addition
def add( n1 , n2 ):
    return n1 + n2
#for Subtraction
def subtract( n1 , n2 ):
    return n1 - n2
#for Multiplication
def multipy( n1 , n2 ):
    return n1 * n2
#for Division
def divide( n1 , n2 ):
    return n1 / n2

  
operation = {
    "+" : "addition",
    "-" : "subtraction",
    "*" : "multiplication",
    "/" : "division"
}

a = int(input("what is the first number? "))
for x in operation:
    print(x)
operator = input("Pick the operator : ")
b = int(input("what is the second number? "))
d = True
while d == True:
    if operator == "+":
        c = add( a , b )
        print(f"{a} {operator} {b} = {c}")
        e = input("Type 'y' if u want to continue with the answer else 'n'. : ")
        if e == "y":
            a = c
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        elif e == "n":
            a = int(input("what is the first number? "))
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        else:
            print("Invalid input")
            d = False
    elif operator == "-":
        c = subtract ( a , b )
        print(f"{a} {operator} {b} = {c}")
        e = input("Type 'y' if u want to continue with the answer else 'n'. : ")
        if e == "y":
            a = c
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        elif e == "n":
            a = int(input("what is the first number? "))
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        else:
            print("Invalid input")
            d = False
    elif operator == "*":
        c = multipy( a , b )
        print(f"{a} {operator} {b} = {c}")
        e = input("Type 'y' if u want to continue with the answer else 'n'. : ")
        if e == "y":
            a = c
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        elif e == "n":
            a = int(input("what is the first number? "))
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        else:
            print("Invalid input")
            d = False
    elif operator == "/":
        c = divide( a , b )
        print(f"{a} {operator} {b} = {c}")
        e = input("Type 'y' if u want to continue with the answer else 'n'. : ")
        if e == "y":
            a = c
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        elif e == "n":
            a = int(input("what is the first number? "))
            operator = input("Pick the operator : ")
            b = int(input("what is the second number? "))
        else:
            print("Invalid input")
            d = False
    else:
        print("Invalid Operator")
        d = False