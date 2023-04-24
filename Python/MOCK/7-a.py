class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        popped_item = temp.data
        del temp
        return popped_item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.display()  # prints 4 3 2 1

print(s.pop())  # prints 4
print(s.peek())  # prints 3
