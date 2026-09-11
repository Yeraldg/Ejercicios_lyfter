
#ejercicio 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
    def dequeue(self):
        
        if self.front is None:
            return None
        remove_node = self.front
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
            
        return remove_node.data
    
    def print_queue(self):
        current = self.front
        print("Queue: ")
        while current is not None:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=" --> ")
            current = current.next

#ejercicio 2

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_back(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        
        while current is not None:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next
    
    def print_linkedl(self):
        current = self.head
        print("linkedlist: ")
        while current is not None:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=" --> ")
            current = current.next

#jercicio 3

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append (self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def prepend(self, data):
        new_node = DoubleNode(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
                return

            self.head.prev = None
            return
        current = self.head
        while current is not None:
            if current.data == data:
                if current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                    return

                current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next

        
    def print_forward(self):
        current = self.head
        print("Forward DoubleLinkedList: ")
        while current is not None:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end="--> ")
            current = current.next
    
    def print_backward(self):
        current = self.tail
        print("Backward DoubleLinkedList: ")
        while current is not None:
            if current.prev is None:
                print(current.data)
            else:
                print(current.data, end=" <--")
            current = current.prev
            




def main():
    #ejercicio 1
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.print_queue()
    print("-----------")
    print(f"Removed node: {q.dequeue()}")
    print(f"Removed node: {q.dequeue()}")
    print(f"Removed node: {q.dequeue()}")
    print(f"Removed node: {q.dequeue()}")
    print("empty queue example: ")
    q.print_queue()
    
    #ejercicio 2
    ll = LinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    ll.insert_back(30)
    print("------------")
    ll.print_linkedl()
    print("------------")
    ll.delete(10)
    ll.delete(20)
    ll.delete(30)
    print("empty Linked1list example: ")
    ll.print_linkedl()
    
    #ejercicio 3
    dll = DoubleLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    print("-----------")
    dll.print_forward()
    dll.print_backward()
    print("-----------")
    dll.prepend("X")
    dll.prepend("Y")
    dll.print_backward()
    print("-----------")
    dll.delete("B")
    print("After deleting B")
    dll.print_forward()
    dll.print_backward()



    
main()

