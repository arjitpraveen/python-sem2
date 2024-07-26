name = input("Enter student's name: ")
usn = input("Enter student's USN: ")

m1 = int(input("Enter subject 1 mark: "))
m2 = int(input("Enter subject 2 mark: "))
m3 = int(input("Enter subject 3 mark: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

print("\nSTUDENT DETAILS:\n-----------------------------------------")
print(f"Name: {name}\nUSN: {usn}\n")
print(f"Subject 1: {m1}\nSubject 2: {m2}\nSubject 3: {m3}")
print("-----------------------------------------")
print(f"Total: {total}/300\nPercentage: {percentage:.2f}%\n")