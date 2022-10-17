def fact(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*fact(n-1)

a = int(input("enter the number to find its factorial: "))
if a >= 0:
    b = fact(a)
    print(f"Factorial of {a} is {b}.")
else:
    print(f"Factorial of {a} cannot be found.")
