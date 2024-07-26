def mean(num):
    return sum(num)/len(num)

def var(num, mean):
    return sum((x - mean) ** 2 for x in num)/len(num)

def std(variance):
    return variance**0.5

n = int(input("Enter the value of N: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

mean_num = mean(numbers)
variance = var(numbers, mean_num)
standard_deviation = std(variance)

print(f"Mean = {mean_num}\nVariance = {variance}\nStandard Deviation = {standard_deviation}")