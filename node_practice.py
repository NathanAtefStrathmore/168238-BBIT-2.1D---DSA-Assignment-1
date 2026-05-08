# Creating a Node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating 3 nodes manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking the nodes
node1.next = node2
node2.next = node3

# Traversing and printing values
current = node1

while current is not None:
    print(current.data)
    current = current.next