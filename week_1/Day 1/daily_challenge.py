number = int(input("Enter the number: "))
length = int(input("Enter the length of numbers: "))

multiples = []

for i in range(1, length+1):
    multiples.append(number * i)
print(multiples)
