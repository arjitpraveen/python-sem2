def DivExp(x, y):
    try:
        z = x / y
        print(f"Quotient = {z}")
    except ZeroDivisionError:
        print("Division by Zero!")

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

DivExp(a, b)