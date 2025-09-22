

#Exercise 1: What is the Season?

month = int(input("Enter a month (1 to 12): "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month entered.")


#Exercise 2: For Loop       
for i in range(1,21):
    print(i)



for index, value in enumerate(range(1, 21)):
    ...
    if index % 2 != 0:
        print((index, value))

#Exercise 3: While Loop
my_name = "ayoub" 

while True:
    name = input("Enter your name: ")
    if name == my_name:
        print("You have entered the correct name.")
        break
    else:
        print("Incorrect name, please try again.")


#Exercise 4: Check the index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name_to_check = input("Enter a name to check: ")
if name_to_check in names:
    index = names.index(name_to_check)
    print(f"{name_to_check} is found at index {index}.")
else:
    print(f"{name_to_check} is not found in the list.")




    #Exercise 5: Greatest Number

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

greatest = max(num_1, num_2, num_3)
print(f"The greatest number is: {greatest}")



#Exercise 6: Random number
import random

wins = 0
losses = 0

while True:
    user_input = input("Enter a number between 1 and 9 (or 'q' to quit): ")

    if user_input.lower() == "q":
        print("Game Over!")
        print(f"Total Wins: {wins}")
        print(f"Total Losses: {losses}")
        break

    user_num = int(user_input)
    random_num = random.randint(1, 9)
    if user_num == random_num:
        print("Winner ")
        wins += 1
    else:
        print(f"Better luck next time! The correct number was {random_num}.")
        losses += 1

