#Challenge 1

number = int(input("Enter the number: "))
length = int(input("Enter the length of numbers: "))

multiples = []

for i in range(1, length+1):
    multiples.append(number * i)
print(multiples)

#hallenge 2

def remove_duplicates(word):
    result = ""
    for char in word:
        if not result or char != result[-1]:
            result += char
    return result

# Ask user for input
user_word = input("Enter a word: ")
print("Result:", remove_duplicates(user_word))
