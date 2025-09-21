class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert at beginning
def insert_at_beginning(head, new_data):
    new_node = Node(new_data)   # Step 1: create a new node
    new_node.next = head        # Step 2: point new node to current head
    head = new_node             # Step 3: update head to the new node
    return head


# Example
head = Node(5)
head.next = Node(9)
head.next.next = Node(2)
head.next.next.next = Node(7)

# Insert 100 at beginning
head = insert_at_beginning(head, 100)


# Print the list
current = head
while current:
    print(current.data, end=" → ")
    current = current.next
