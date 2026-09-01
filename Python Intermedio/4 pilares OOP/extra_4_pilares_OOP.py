from abc import ABC, abstractmethod

# ejercicio 1

class Employee:
    def __init__( self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
            if value < 0:
                raise ValueError ("salary can not be negative.")
            else:
                self._salary = value
    
    def promote( self, percentage):
        amount_to_promote = self.salary * percentage
        self.salary = self.salary + amount_to_promote
        return self.salary
    
#ejercicio 2
    
class User(ABC):
    
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self, permission):
        pass
    
class AdminUser(User):
    def __init__(self, name):
        self.name = name
    
    def get_role(self):
        return "Admin"
    
    def has_permission( self, permission):
        return True
    
class RegularUser(User):
    def __init__(self, name):
            self.name = name
    
    def get_role(self):
        return "Regular User" 
    
    def has_permission(self, permission):
        if permission == "read":
            return True
        else:
            return False
        
#ejercicio 3

class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        
    @property
    def brand(self):
        return self._brand
    
    @property
    def year(self):
        return self._year
    
    def get_info(self):
        return f"{self._brand}, {self._year}"
    
class Car(Vehicle):
    def __init__(self,brand, year, model):
        super().__init__(brand, year)
        self.model = model
        
    def get_info(self):
        return f"{self._brand}, {self._year}, {self.model}."
    
class Motorcycle(Vehicle):
    def __init__(self,brand, year, moto_type):
        super().__init__(brand, year)
        self.moto_type = moto_type
        
    def get_info(self):
        return f"{self._brand}, {self._year}, {self.moto_type}."
        
    
def main():
    #ejercicio 1
    employee = Employee("Ana", 1000)
    print(f"Employee name: {employee.name}")
    print(f"Employee salary: {employee.salary}")
    employee.promote(0.1)
    print(f"New salary: {employee.salary}")
    
    try:
        employee.salary = -500
    except ValueError as error:
        print(error)
        
    #ejercicio 2
    print("-----------")
    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")
    print(user1.get_role())
    print(user1.has_permission("delete"))
    print("------")
    print(user2.get_role())
    print(user2.has_permission("delete"))
    print(user2.has_permission("read"))
    
    #ejercicio 3
    vehicle1 = Car("Toyota", 2020, "Corolla")
    vehicle2 = Motorcycle("Yamaha", 2022, "Sport")
    print("-----------")
    print(vehicle1.get_info())
    print(vehicle2.get_info())
    
main()
