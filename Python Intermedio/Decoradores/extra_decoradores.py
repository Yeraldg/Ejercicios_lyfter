from datetime import datetime
from functools import wraps

#ejericio 1
def repeat_twice(function):
    def wrapper (*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
        
    return wrapper

@repeat_twice
def hello(name):
    print (f"Hello {name}")
    
#ejercicio 2

user_logged_in = False #se que va al inicio del archivo pero la coloque aqui para llevar el orden de los ejericios
    
def requires_login(function):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise ValueError("User not authenticated")
        function(*args, **kwargs)
        
    return wrapper

@requires_login
def view_profile():
    print("Showing User Profile")
    
#ejercicio 3

def log_call(function):
    def wrapper (*args, **kwargs):
        result = function(*args, **kwargs)
        print(f"func: {function.__name__} - arguements: {args} - {datetime.now()} - Result: {result}")
        return result
    return wrapper


def validate_numbers(function):
    @wraps(function)
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

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

def main():
    #ejercicio 1
    hello("Carlos")
    
    #ejercicio 2
    try:
        view_profile()
    except ValueError as error:
        print(error)
        
    #ejercicio 3
    print(multiply(3, 4))


main()