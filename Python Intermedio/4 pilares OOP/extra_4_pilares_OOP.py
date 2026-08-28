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
    
main()
        