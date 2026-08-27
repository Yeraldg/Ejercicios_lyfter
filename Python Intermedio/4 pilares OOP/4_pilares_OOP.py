from abc import ABC, abstractmethod
import math

# ejercicio 1

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit_amount(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw_amount(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
        
    def withdraw_amount(self, amount):
        if (self.balance - amount) <= self.min_balance:
            raise ValueError (f"Minimum balance: {self.min_balance} required, unable to withdraw: {amount}")
        else:
            self.balance = self.balance - amount
            return self.balance
        
#ejercicio 2

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
            pass
    
    @abstractmethod
    def calculate_area(self):
            pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def calculate_area(self):
        area = math.pi * self.radius**2
        return area
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter
    
    def calculate_area(self):
        area = self.side**2
        return area
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def calculate_area(self):
        area = self.width * self.height
        return area

#jercicio 3
#Herecia multiple
#funcion:
#1. combinar capacidades
#2. Clases apartir de comportamientos
#A. clases Mixin(agrega capacidad ocomportamientos)*no es que, es que puede hacer
#b.composicion(una clase dentro de una clase)
#3.Resolver comportamientos compartidos
#ejemplo solicitado:
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

class C(A):
    def hello(self):
        print("C")

class D(B, C):
    pass

def main():
    #ejercicio 1
    account = BankAccount(5000)
    account.deposit_amount(1000)
    print(f"Bank account balance: {account.balance}")
    account.withdraw_amount(2000)
    print(f"Bank account balance: {account.balance}")
    savings_account = SavingsAccount(account.balance, 2000)
    savings_account.deposit_amount(1000)
    print(f"Savings account balance: {savings_account.balance}")
    savings_account.withdraw_amount(2500)
    print(f"Savings account balance: {savings_account.balance}")

    try:
        savings_account.withdraw_amount(2000)
    except ValueError as error:
        print(error)
    #ejercicio 2
    print("--------")
    circle = Circle(20)
    area1 = circle.calculate_area()
    perimeter1 = circle.calculate_perimeter()
    print("Circle info: ")
    print(f"the area is: {area1}")
    print(f"the perimeter is: {perimeter1}")
    
    square = Square(10)
    area2 = square.calculate_area()
    perimeter2 = square.calculate_perimeter()
    print("Square info: ")
    print(f"the area is: {area2}")
    print(f"the perimeter is: {perimeter2}")
        
    rectangle = Rectangle(20, 30)
    area3 = rectangle.calculate_area()
    perimeter3 = rectangle.calculate_perimeter()
    print("Rectangle info: ")
    print(f"the area is: {area3}")
    print(f"the perimeter is: {perimeter3}")
    #ejercicio 3
    print("-------")
    d = D()
    d.hello()

main()