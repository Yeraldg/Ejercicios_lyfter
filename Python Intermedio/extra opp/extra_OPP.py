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
    
def get_rectangle_values():

    while True:
        try:
            width = int(input("please enter the width: ").strip())
            height = int(input("please enter the height: ").strip())
            valid_values = True
            for value in (width, height):
                if value <= 0:
                    print("please enter a digit greater than 0")
                    valid_values = False
                    break
            if not valid_values:
                continue
            return width, height
        
        except ValueError:
            print("Please enter a valid format number.")
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
    
    
#ejercicio 3

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def show_products(self):
        print("Products on the inventory:")
        for product in self.products:
            print(f"Name: {product.name}")
            print(f"Price: {product.price}")
            print(f"Quantity: {product.quantity} units.")
            print("--------------")
            
    def calculate_total_inventory_value(self):
        total_value = 0
        for product in self.products:
            product_value = product.price * product.quantity
            total_value += product_value
        return total_value

        


def main():
    width, height = get_rectangle_values()
    rectangle = Rectangle(width, height)
    area = rectangle.get_area()
    perimeter = rectangle.get_perimeter()
    print(f"the area is: {area}")
    print(f"the perimeter is: {perimeter}")
    
    dog = Dog("firulais")
    print(f"the dog's name is: {dog.name}")
    print(dog.speak())
    cat = Cat("Papi")
    print(f"the cat's name is: {cat.name}")
    print(cat.speak())
    
    product1 = Product("Mouse", 5000, 3)
    product2 = Product("keyboard", 8000, 2)
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)
    print("Mouse and keyboard added")
    

    inventory.show_products()
    
    total = inventory.calculate_total_inventory_value()
    print(f"Total value of entire inventory: {total}")
    
main()



