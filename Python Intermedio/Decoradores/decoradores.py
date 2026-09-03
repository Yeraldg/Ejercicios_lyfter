from datetime import date

#ejercicio 1

def show_info(function):
    def wrapper (*args, **kwargs):
        print(f"arguements: {args}")
        print(f"keyword arguments: {kwargs}")
        
        result = function(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@show_info
def add(a, b):
    return a + b

#ejericio 2

def only_numbers(function):
    def wrapper (*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be numbers")
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("All arguments must be numbers")
        result = function(*args, **kwargs)
        return result
    return wrapper
    
@only_numbers
def check(a, b):
    return a + b

#ejercicio 3

class User:
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if(today.month, today.day) < (self.date_of_birth.month,self.date_of_birth.day):
            age -= 1
        return age
            
def adult_only(function):
    def wrapper (*args, **kwargs):
        user = args [0]
        if user.age < 18:
            raise ValueError ("User under 18.")
        return function(*args, **kwargs)
    return wrapper

@adult_only
def access(user):
        return "Access granted"

def main():
    #ejercicio 1
    add (3 , 5)
    print("---------")
    add(a=3, b=5)
    
    #ejercicio 2
    check (3 , 5)
    print("---------")
    check (a=3, b=5)
    try:
        check(3, "5")
    except ValueError as error:
        print(error)
        
    #ejercicio 3
    print("------------")
    adult = User(date(2000, 1, 1))
    minor = User(date(2010, 1, 1))
    print(access(adult))
    try:
        print(access(minor))
    except ValueError as error:
        print(error)


main()