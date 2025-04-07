class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return 'Stack is empty'
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

s1 = Stack()
print(s1.pop())
s1.push("Data structure")
s1.push("Database")
print(s1.pop())
print(s1.pop())
