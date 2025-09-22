#Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Mufasa", 2)
cat2 = Cat("Scar", 5)
cat3 = Cat("Nala", 3)

def find_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)

oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print("Both dogs are the same height.")

#Exercise 3 : Who’s the song producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        self.animal_groups = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = [animal]
            else:
                self.animal_groups[first_letter].append(animal)
        return self.animal_groups

    def get_groups(self):
        print("Animal groups:")
        for key in sorted(self.animal_groups):
            print(f"{key}: {self.animal_groups[key]}")

new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.get_animals()
new_york_zoo.sell_animal("Eel")
new_york_zoo.get_animals()
new_york_zoo.sort_animals()
new_york_zoo.get_groups()
