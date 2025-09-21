class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to count length
def length_of_linked_list(head):
    count = 0
    current = head   # start from head
    while current is not None:
        count += 1          # visit this node
        current = current.next  # move to next node
    return count

# Example linked list: 5 → 9 → 2 → 7
head = Node(5)
head.next = Node(9)
head.next.next = Node(2)
head.next.next.next = Node(7)

print("Length:", length_of_linked_list(head))  # Output: 4
