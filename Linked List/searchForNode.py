class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to search a value
def search(head, target):
    current = head
    position = 0               # To track index (optional)
    
    while current:             # Traverse until end
        if current.data == target:
            return f"Found at position {position}"
        current = current.next
        position += 1
    
    return "Not found"


# Example
head = Node(5)
head.next = Node(9)
head.next.next = Node(2)
head.next.next.next = Node(7)

print(search(head, 2))   # Found at position 2
print(search(head, 10))  # Not found
