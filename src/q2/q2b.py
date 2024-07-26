def fact(x):

    if x == 1:
        return 1
    else:
        return (x*fact(x - 1))
    

n = int(input("Enter N: "))
r = int(input("Enter R: "))
m = n - r

factn = fact(n)
factr = fact(r)
factm = fact(m)

bio = factn / (factr*factm)

print(f"N factorial is: {factn}")
print(f"R factorial is: {factr}")
print(f"Binomial Coefficient series is: {bio}")
