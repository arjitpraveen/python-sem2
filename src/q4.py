num = input("Enter a multidigit number: ")

dict = {}

for x in num:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

print(str(dict))