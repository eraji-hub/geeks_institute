import random


#🌟 Exercise 1 : Pets
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

bengal_cat = Bengal("Leo", 3)
chartreux_cat = Chartreux("Milo", 5)
siamese_cat = Siamese("Luna", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()


#🌟 Exercise 2 : Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 4, 25)

print(dog1.bark())
print(dog2.bark())

print(f"{dog1.name} speed: {dog1.run_speed():.2f}")
print(f"{dog2.name} speed: {dog2.run_speed():.2f}")

print(dog1.fight(dog2))

#🌟 Exercise 3 : Dogs Domesticated

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet")

dog1 = PetDog("Rex", 5, 20)
dog2 = PetDog("Buddy", 4, 25)
dog3 = PetDog("Charlie", 3, 15)

dog1.train()
dog1.do_a_trick()

dog1.play(dog2, dog3)
dog2.do_a_trick()  

#Exercise 4 : Family

class Family:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs.get('name')} has been born into the {self.last_name} family!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        print(f"{name} is not in the family.")
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(member)

members_list = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

smith_family = Family("Smith", members_list)

smith_family.family_presentation()
print(smith_family.is_18("Michael"))  
print(smith_family.is_18("Sarah"))    
print(smith_family.is_18("Tom"))  


#Exercise 5 : TheIncredibles Family

class Family:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs.get('name')} has been born into the {self.last_name} family!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        print(f"{name} is not in the family.")
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(member)

class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} uses their power: {member.get('power')}")
                else:
                    raise Exception(f"{name} is not over 18 years old!")
                return
        print(f"{name} is not in the family.")

    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()

members_list = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

incredibles_family = TheIncredibles("Incredibles", members_list)
incredibles_family.incredible_presentation()
incredibles_family.use_power("Michael")
incredibles_family.use_power("Sarah")
incredibles_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")
incredibles_family.incredible_presentation()

try:
    incredibles_family.use_power("Jack")
except Exception as e:
    print(e)
