class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list: 1 → 2 → 3 → 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Traverse and print
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
