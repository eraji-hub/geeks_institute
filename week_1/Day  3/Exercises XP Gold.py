import random



#Exercise 1 : Geometry
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is a set of points in a plane that are at a given distance from a given point, the center.")

c1 = Circle()  
c2 = Circle(5)  

print(f"Circle with radius {c1.radius}: perimeter = {c1.perimeter():.2f}, area = {c1.area():.2f}")
print(f"Circle with radius {c2.radius}: perimeter = {c2.perimeter():.2f}, area = {c2.area():.2f}")

c1.definition()

#Exercise 2 : Custom List Class

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def get_reversed(self):
        return self.letters[::-1]

    def get_sorted(self):
        return sorted(self.letters)

    def random_numbers_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]

mylist = MyList(['d', 'a', 'c', 'b'])

print("Original list:", mylist.letters)
print("Reversed list:", mylist.get_reversed())
print("Sorted list:", mylist.get_sorted())
print("Random numbers list:", mylist.random_numbers_list())


#Exercise 3 : Restaurant Menu Manager

class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        new_dish = {"name": name, "price": price, "spice_level": spice, "gluten": gluten}
        self.menu.append(new_dish)
        print(f"{name} added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice_level"] = spice
                dish["gluten"] = gluten
                print(f"{name} updated successfully.")
                return
        print(f"{name} is not in the menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} removed. Updated menu:")
                for d in self.menu:
                    print(d)
                return
        print(f"{name} is not in the menu.")

if __name__ == "__main__":
    manager = MenuManager()
    
    manager.add_item("Pasta", 12, "A", True)
    
    manager.update_item("Salad", 20, "B", False)
    
    manager.remove_item("Soup")
