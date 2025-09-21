class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert at the end
def insert_at_end(head, new_data):
    new_node = Node(new_data)   # Step 1: create a new node
    
    if head is None:            # If list is empty, new node becomes head
        return new_node

    current = head
    while current.next:         # Step 2: traverse to the last node
        current = current.next

    current.next = new_node     # Step 3: attach new node at the end
    return head


# Example
head = Node(5)
head.next = Node(9)
head.next.next = Node(2)
head.next.next.next = Node(7)

# Insert 100 at end
head = insert_at_end(head, 100)


# Print the list
current = head
while current:
    print(current.data, end=" → ")
    current = current.next
