#ejercicio 1 y 2

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        #para la parte de Deque 
        self.prev = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push (self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def push_node(self, node):
        node.next = self.top
        self.top = node
    
    def print_stack(self):
        current = self.top
        print("Stack: ")
        while current is not None:
            print(current.value)
            current = current.next
            
    def pop(self):
        if self.top is None:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
    
    def pop_node(self):
        if self.top is None:
            return None
        removed_node = self.top
        self.top = self.top.next
        removed_node.next = None
        return removed_node
    
    def swap_nodes(self, previous, first, second):
        first.next = second.next
        second.next = first
        if previous is None:
            self.top = second
        else:
            previous.next = second
            
    def bubble_sort(self):
        iterations = 0
        swaps = 0
        avoid_to_repeat = True
        while avoid_to_repeat:
            iterations += 1
            previous = None
            current = self.top
            avoid_to_repeat = False
            while current is not None and current.next is not None:
                next_node = current.next
                print("Current: ", current.value)
                print("Next: ", next_node.value)
                if current.value > next_node.value:
                    print("Swap needed")
                    self.swap_nodes(previous, current, next_node)
                    swaps += 1
                    previous = next_node
                    avoid_to_repeat = True
                else:
                    previous = current
                    current = current.next
        return iterations, swaps

class Deque:
    def __init__(self):
        self.left = None
        self.right = None
        
    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
    
    def print_deque(self):
        current = self.left
        print("Deque: ")
        while current is not None:
            print(current.value)
            current = current.next
            
    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.right = new_node
            self.left = new_node
        else:
            self.right.next = new_node
            new_node.prev = self.right
            self.right = new_node
            
    def pop_left(self):
        if self.left is None:
            return None
        removed_node = self.left
        self.left = self.left.next
        
        if self.left is not None:
            self.left.prev = None
        else:
            self.right = None
        return removed_node.value
    
    def pop_right(self):
        if self.right is None:
            return None
        removed_node = self.right
        self.right = self.right.prev
        if self.right is not None:
            self.right.next = None
        else:
            self.left = None
        return removed_node.value
    
    def swap_nodes(self, previous, first, second):
        after_second = second.next
        if previous is None:
            self.left = second
        else:
            previous.next = second
        second.prev = previous
        second.next = first
        
        first.prev = second
        first.next =after_second
        
        if after_second is not None:
            after_second.prev = first
        else:
            self.right = first
            
    def bubble_sort(self):
        iterations = 0
        swaps = 0
        
        avoid_to_repeat = True
        while avoid_to_repeat:
            iterations += 1
            previous = None
            first = self.left
            avoid_to_repeat = False
            while first is not None and first.next is not None:
                second = first.next
                print(f"Current: {first.value}")
                print(f"Next: {second.value}")
                if first.value > second.value:
                    print("Swap needed")
                    self.swap_nodes(previous, first, second)
                    swaps += 1
                    previous = second
                    avoid_to_repeat = True
                else:
                    previous = first
                    first = first.next
        return iterations, swaps

#ejrcicio 3

def get_list_amount():
    while True:
        try:
            list_amount = input("how many numbers should the list have?: ")
            if not list_amount.isdigit():
                raise ValueError("please use numerical format only")
            if int(list_amount) == 0:
                raise ValueError("the list can not be empty")
            break
        except ValueError as error:
            print(error)
    return int(list_amount)
            
def get_list_to_sort():
    elements = get_list_amount()
    list_to_sort = []
    counter = 1
    while counter <= elements:
        try:
            element_to_sort = input(f"please enter the {counter} number: ")
            if not element_to_sort.lstrip("-").isdigit():
                raise ValueError("please use numerical format only")
            element_to_sort = int(element_to_sort)
            list_to_sort.append(element_to_sort)
            counter += 1
        except ValueError as error:
            print(error)
    return list_to_sort

def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):
        avoid_to_repeat = False
        for index in range(0, len(list_to_sort) -1):
                current_element = list_to_sort[index]
                next_element = list_to_sort[index +1]
                if current_element > next_element:
                    list_to_sort[index] = next_element
                    list_to_sort[index +1] = current_element 
                    avoid_to_repeat = True
        if not avoid_to_repeat:
            return list_to_sort
    return list_to_sort
    
    
def main():
    stack = Stack()
    stack.push(-10)
    stack.push(40)
    stack.push(-5)
    stack.push(40)
    print("Before change:")
    stack.print_stack()
    
    print("Checking pairs: ")
    iterations, swaps = stack.bubble_sort()
    stack.print_stack()
    print("Iterations: ", iterations)
    print("Swaps: ", swaps)
    
    deque = Deque()
    
    deque.push_right(60)
    deque.push_right(40)
    deque.push_right(50)
    print("Before change:")
    deque.print_deque()
    
    print("Checking pairs: ")
    iterations, swaps = deque.bubble_sort()
    deque.print_deque()
    print("Iterations: ", iterations)
    print("Swaps: ", swaps)
    print("------------")
    list_to_sort = get_list_to_sort()
    sorted_list = bubble_sort(list_to_sort)
    print(f"the sorted list is: {sorted_list}")
main()