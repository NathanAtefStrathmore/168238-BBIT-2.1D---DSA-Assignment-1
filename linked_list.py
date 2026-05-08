class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Display all nodes
    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    # Search for a value
    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False


# Testing the LinkedList

my_list = LinkedList()

my_list.append(5)
my_list.append(15)
my_list.append(25)

print("Linked List:")
my_list.display()

print("Search 15:", my_list.search(15))
print("Search 100:", my_list.search(100))