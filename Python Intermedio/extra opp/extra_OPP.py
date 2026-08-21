#ejercicio 1

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        area = self.width * self.height
        
        return area
        
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        
        return perimeter
    
def  get_rectangle_values():

    while True:
        try:
            width = int(input("please enter the width: ").strip())
            height = int(input("please enter the height: ").strip())
            valid_values = True
            for value in (width, height):
                if value <= 0:
                    print("please entre a digit greater than 0")
                    valid_values = False
                    break
            if not valid_values:
                continue
            return width, height
        
        except ValueError:
            print("please use only a number format.")
            continue
        
        
#ejercicio 2

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "make a sound"
    
class Dog(Animal):
    def speak(self):
        return "Guau"
    
class Cat(Animal):
    def speak(self):
        return "Miau"


def main():
    width, height = get_rectangle_values()
    rectangle = Rectangle(width,height)
    area = rectangle.get_area()
    perimeter = rectangle.get_perimeter()
    print(f" the area is: {area}")
    print(f" the perimeter is: {perimeter}")
    
    dog = Dog("firulais")
    print(f"the dog's name is: {dog.name}")
    print(dog.speak())
    cat = Cat("Papi")
    print(f"the cat's name is: {cat.name}")
    print(cat.speak())
    
main()



