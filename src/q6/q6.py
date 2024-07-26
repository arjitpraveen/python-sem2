fname = input("Enter the file name: ")
words = []

fp = open(fname, 'r')

for line in fp:
    
    string = line.lower().replace(',', '').replace('.', '').split(" ")

    for i in range(len(string)):
        words.append(string[i])

words.sort()

print(f"Sorted list:\n{words}")

fo = open(r"C:\Users\arjit\Downloads\pysem2\q6\q6sorted.txt", 'w')

for item in words:
    fo.write(f"{item}\n")

fo.close()

