class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

    def insert_middle(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            # Find the middle node using slow and fast pointers
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next

            # Insert the new node after the middle node
            new_node = Node(data)
            new_node.next = slow.next
            slow.next = new_node


linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(4)
linked_list.add_node(5)

linked_list.print_list()

linked_list.insert_middle(3)

linked_list.print_list()
