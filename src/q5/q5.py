import operator as op

fname = input("Enter file name: ")
list = {}

fp = open(fname, 'r')

for line in fp:
    
    string = line.lower().replace(',', '').replace('.', '').split(" ")

    for word in string:
        
        if word in list:
            list[word] += 1
        else:
            list[word] = 1

print(f"Words before sorting: \n {str(list)}\n")

sorted_list = dict(sorted(list.items(), key = op.itemgetter(1), reverse = True) [:10])

print(f"10 most occuring words in descending order: \n{sorted_list}")