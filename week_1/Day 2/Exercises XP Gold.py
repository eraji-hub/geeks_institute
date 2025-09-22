
import random



# Exercise 1: Birthday Look-up
birthdays = {
    "Ayoub": "1995/07/14",
    "Oussama": "1990/03/22",
    "soufian": "1985/12/05",
    "sara": "2000/01/30",
    "khadija": "1998/09/17"
}

print("Welcome! You can look up the birthdays of the people in the list!")
name = input("Who's birthday do you want to look up? ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, I don’t have the birthday information for {name}.")

#Exercise 2: Birthdays Advanced 
birthdays = {
    "Ayoub": "1995/07/14",
    "Oussama": "1990/03/22",
    "Soufian": "1985/12/05",
    "Sara": "2000/01/30",
    "Khadija": "1998/09/17"
}

print("Welcome! You can look up the birthdays of the people in the list!")
print("We know the birthdays of: ")
for person in birthdays:
    print(person)

name = input("Whose birthday do you want to look up? ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

#Exercise 3: Sum 


def numbers_sum(X):
    X_str = str(X)
    num1 = int(X_str)   
    num2 = int(X_str * 2)    
    num3 = int(X_str * 3)   
    num4 = int(X_str * 4)    
    
    return num1 + num2 + num3 + num4

print(numbers_sum(3))   
print(numbers_sum(5))  


#Exercise 4: Double Dice


def throw_dice():
    return random.randint(1, 6)
def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:  
            break
    return count


def main():
    results = []
    
   
    for _ in range(100):
        throws = throw_until_doubles()
        results.append(throws)
    
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()

