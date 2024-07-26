name = input("Enter name: ")
yob = int(input("Enter year of birth: "))

senior = 2024 - yob

print(f"Hello, {name}")

if senior >= 55:
    print(f"Age: {senior}\nYou are a senior citizen")
else:
    print(f"Age: {senior}\nYou are NOT a senior citizen")