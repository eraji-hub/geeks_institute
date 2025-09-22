import math 
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=12)

    print(c1)                 
    print(c2)                  
    print("Area of c1:", c1.area())
    print("Area of c2:", c2.area())

    c3 = c1 + c2             
    print("c3 (sum):", c3)

    print("c1 > c2?", c1 > c2)
    print("c1 == c2?", c1 == c2)

  
    circles = [c1, c2, c3]
    circles.sort()
    print("Sorted circles:", circles)
