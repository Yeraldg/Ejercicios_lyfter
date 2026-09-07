#ejercicio 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        #ejercicio 2* 
        self.prev = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push (self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
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
        
# ejericio 2

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
    
#ejercicio 3

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def print_tree(self):
        print("Binary Tree: ")
        self.print_node(self.root)
    
    def print_node(self, node):
        if node is None:
            return
        print(node.value)
        self.print_node(node.left)
        self.print_node(node.right)

def main():
    #ejercicio 1
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    print("---------")
    print(f"Removed node: {stack.pop()}")
    print("---------")
    stack.print_stack()
    print("---------")
    print(f"Removed node: {stack.pop()}")
    print(f"Removed node: {stack.pop()}")
    print(f"Removed node: {stack.pop()}")
    
    # ejercicio 2
    print("---------")
    deque = Deque()
    deque.push_left(0)
    deque.push_left(-10)
    deque.push_left(-20)
    deque.print_deque()
    print("---------")
    deque.push_right(10)
    deque.push_right(20)
    deque.print_deque()
    print("---------")
    print(f"Removed node: {deque.pop_left()}")
    deque.print_deque()
    print("---------")
    print(f"Removed node: {deque.pop_right()}")
    deque.print_deque()
    print("---------")
    print(f"Removed node: {deque.pop_left()}")
    print(f"Removed node: {deque.pop_left()}")
    print(f"Removed node: {deque.pop_left()}")
    print(f"Removed node: {deque.pop_left()}")
    deque.print_deque()
    
    # ejercicio 3
    print("---------")
    tree = BinaryTree()
    tree.root = TreeNode(0)
    tree.root.left = TreeNode(-10)
    tree.root.right = TreeNode(10)
    tree.print_tree()
    
main()