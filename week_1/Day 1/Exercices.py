#Exercise 1 : Hello World

print('Hello world\n'*4)

#Exercise 2 : Some Math

print(pow(99,3)*8)

#🌟 Exercise 3 : What’s your name ?

name = input("What's your name? ")

my_name = "ayoub"

if name.lower() == my_name.lower():
    print(f"Wow! We have the same name, {name} Are we long-lost twins?")
else:
    print(f"Nice to meet you,  { name } Don't worry, having a different name makes you unique")


#Exercise 4 : Tall enough to ride a roller coaster

height = int(input("Enter your height in cm: "))
if height >= 145:
    print("You are tall enough to ride the rollear coaster!")
else:
    print("Sorry, you are not tall enough to ride the roller coaster.")

#Exercise 5 : Favorite Numbers


my_fav_numbers = {1,8,15,22,42,69,100,420,1000}  # set
my_fav_numbers.add(7)
my_fav_numbers.add(13)
my_fav_numbers.add(21)
my_fav_numbers.discard(1)

friend_fav_numbers = {3,6,9,12,15,18,21,24,27}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# Exercise 6: Tuple : is immutable
my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple)
new_tuple = my_tuple + (11,12,13)
print(new_tuple)

# Exercise 7: List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
count_apples = basket.count("Apples")
print(f"Number of Apples in the basket: {count_apples}")
basket.clear()
print(basket)  

# 🌟 Exercise 8 : Sandwich Orders

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]


while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    print("Sorry, we are out of Pastrami sandwich.")
    print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

    