import random



# Exercise 1 : Convert lists into dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

 # Exercise 2: Cinemax

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8 , "jerry": 2}

for name, age in family.items():
     if age < 3:
         price = 0
         print(f"{name} Your ticket is free  : ${price}")
     elif 3 <= age < 12:
         price = 10
     else:
         price = 15
     print(f"{name} has to pay : ${price}")
     family[name] = price
total_cost = sum(family.values())
print(f"Total cost for the family: ${total_cost}")


  # Exercise 3 : Zara
brand = {
     "name": "Zara",
     "creation_date": 1975,
     "creator_name": "Amancio Ortega Gaona",
     "type_of_clothes": "Fast Fashion", 
     "international_competitors": ["Gap", "H&M", "Benetton"],
     "number_stores": 7000,
     "major_color": {
         "France": "blue",
         "Spain": "red",
         "US": ["pink", "green"]
     }
 }
print(brand)
brand["number_stores"] = 2000
print(f"Updated number of stores: {brand['number_stores']}")
brand["type_of_clothes"] = "Casual"
print(f"Updated type of clothes: {brand['type_of_clothes']}")
print(f"Major colors in the US: {brand['major_color']['US']}")
print(f"Last international competitor: {brand['international_competitors'][-1]}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
     brand["international_competitors"].append("Desigual")
print(brand)
del brand["creation_date"]
print(brand)
print(f"Number of key-value pairs in the brand dictionary: {len(brand)}")
print(brand.keys())
more_on_zara = {
     "creation_date": 1975,
     "number_stores": 10000
 }
brand.update(more_on_zara)
print(brand["number_stores"])
print(brand)




#exercices4 

def describe_city(city):  
    return city 

def describe_country(country="Spain"):
    return country   

print(describe_city("Casablanca"), "is in", describe_country("Morroco"))

#exrcises 5 

import random   

def check_number(user_num):
    random_num = random.randint(1, 100)

    if user_num == random_num:
        print("Success!  The numbers are the same.")
    else:
        print("Fail")
        print("Your number:", user_num)
        print("Random number:", random_num)
check_number(50)


#exrcises 6
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'")

make_shirt()

make_shirt("Medium")

make_shirt("Small", "Code every day!")

make_shirt(size="XL", text="Debugging mode ON")
make_shirt(text="Custom message!", size="M")

 #exrcises 7 


import random

def get_random_temp():
    return random.randint(-10, 40)  

def main():
    temp = get_random_temp()  
    print(f"The temperature right now is {temp}°C")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today ")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat ")
    elif 16 < temp <= 23:
        print("Nice weather! A light jacket should be fine")
    elif 24 <= temp <= 32:
        print("Warm weather! Stay hydrated ")
    else:  
        print("It’s really hot! Wear sunscreen and stay cool ")


main()



 #exrcises 8


data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []  

    for item in data:
        user_answer = input(item["question"] + " ")

        if user_answer.strip().lower() == item["answer"].lower():
            print(" Correct!\n")
            correct += 1
        else:
            print(f"Wrong! The correct answer was: {item['answer']}\n")
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return correct, incorrect, wrong_answers

def show_results(correct, incorrect, wrong_answers):
    print("Results:")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if incorrect > 0:
        print(" You got some wrong answers:")
        for w in wrong_answers:
            print(f"Q: {w['question']}")
            print(f"   Your answer: {w['your_answer']}")
            print(f"   Correct answer: {w['correct_answer']}\n")

    if incorrect > 3:
        print("You had more than 3 wrong answers. Let's play again!\n")
        main() 



def main():
    correct, incorrect, wrong_answers = ask_questions()
    show_results(correct, incorrect, wrong_answers)


main()
