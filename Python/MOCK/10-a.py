class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_in_middle(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the linked list.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# create a linked list
llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Original linked list:")
llist.print_list()

# insert a new node in the middle
llist.insert_in_middle(llist.head.next, 5)

print("\nLinked list after inserting a new node:")
llist.print_list()