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
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            return popped_node.data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data


stack = [1, 2, 3]

print(stack.pop())  # remove and print the top item (3)
print(stack.pop())  # remove and print the top item (2)
print(stack.pop())  # remove and print the top item (1)
