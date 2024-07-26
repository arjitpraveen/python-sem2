n = int(input("Enter n value: "))

a, b, i = 0, 1, 1

print("The fibonacci sequence is:\n")

while i <= n:
    c = a + b
    print(f"\t{c}")

    a = b
    b = c
    i += 1