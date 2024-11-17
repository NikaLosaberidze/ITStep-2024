class Stack:
    def __init__(self):
        self.stack = []

    #TODO Use list append method to add element
    def push(self, data):
       self.stack.append(data)
       

    #TODO Use list pop method to remove element
    def pop(self):
        if self.stack == []:
            raise Exception("Stack is already empty!")
            return
        del self.stack[-1]


class Node:

    def __init__(self, value=0) -> None:
        self.value = value
        self.next = None

    
class LinkedList:
    
    def __init__(self,) -> None:
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return

        curr_head = self.head
        while curr_head.next:
            curr_head = curr_head.next

        curr_head.next = Node(value)

    def remove(self):
        if not self.head:
            raise Exception("Nothing To Remove...")
            return
        
        curr_head = self.head
        if not curr_head.next:
            self.head = None
            return
         
        while curr_head.next.next:
            curr_head = curr_head.next
        
        curr_head.next = None
