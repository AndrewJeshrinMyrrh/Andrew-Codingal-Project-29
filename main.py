class Circle:
    PI = 3.142
    
    def __init__(self, radius):
        self.radius = radius
        
    def area (self):
        return (Circle.PI * self.radius * self.radius)
    
    def circumference(self):
        return (2 * Circle.PI * self.radius)
    
r = int(input("Enter the radius of Circle: "))
C = Circle(r)
print("Area of Circle is: ", C.area())
print("Perimeter of Circle is: ", C.circumference())
print("")
        