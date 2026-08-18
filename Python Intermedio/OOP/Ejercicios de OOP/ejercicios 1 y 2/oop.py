#ejercicio 1

class Circle:
    radius =  20
    
    def get_area(self):
        area = 3.14 *(self.radius ** 2)
        
        return area
    
circle1 = Circle()
print(circle1.get_area())

#ejercicio 2

class Bus:
    max_passengers = 10
    passengers = []
    def add_passenger(self, person):

        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"passenger added: {person.name}")
        else:
            print("sorry, the bus is full")
            
    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print (f"that person was removed from the bus: {person.name}")
        else:
            print("that person is not a passenger in this bus")
    
class Person:

    def __init__(self, name):
        self.name = name
        
def main():
    bus = Bus()

    person1 = Person("John")
    person2 = Person("Maria")
    
    bus.add_passenger(person1)
    bus.add_passenger(person2)
    
    bus.remove_passenger(person1)
    
main()
