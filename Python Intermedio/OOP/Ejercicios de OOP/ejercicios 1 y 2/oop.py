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
    def __init__(self):
        self.max_passengers = 10
        self.passengers = []
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
        
def create_bus():
    bus = Bus()

    person1 = Person("John")
    person2 = Person("Maria")
    
    bus.add_passenger(person1)
    bus.add_passenger(person2)
    
    bus.remove_passenger(person1)
    

#ejercicio 4

class Head:
    pass

class Hand:
    pass

class Feet:
    pass

class Arm:
    def __init__(self, hand):
        self.hand = hand
        
class Leg:
    def __init__(self, feet):
        self.feet = feet
        
class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        
class Human:
    def __init__(self, torso):
        self.torso = torso
        
def create_body_parts():
    head = Head()
    right_hand = Hand()
    left_hand = Hand()
    right_feet = Feet()
    left_feet = Feet()

    return head, right_hand, left_hand, right_feet, left_feet

def assemble_body(head, right_hand, left_hand, right_feet, left_feet):
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)
    right_leg = Leg(right_feet)
    left_leg = Leg(left_feet)
    
    return Torso( head, right_arm, left_arm, right_leg, left_leg)
        
def create_human():
    head, right_hand, left_hand, right_feet, left_feet = create_body_parts()

    torso = assemble_body( head, right_hand, left_hand, right_feet, left_feet)

    human = Human(torso)

    return human





def main():
    create_bus()
    create_human()
    
main()
