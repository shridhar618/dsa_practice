class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSameTree(p, q):
    # If both are None → trees are same
    if not p and not q:
        return True
    
    # If one is None but not the other → trees differ
    if not p or not q:
        return False
    
    # Check if current values are same
    if p.data != q.data:
        return False
    
    # Recursively check left & right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Example Trees
# Tree 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Tree 2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print(isSameTree(root1, root2))  # True
