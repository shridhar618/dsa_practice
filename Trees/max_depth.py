class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(root):
    if root is None:  # base case
        return 0

    # Recursively find depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Height of tree = max of left/right + 1 (for root)
    return max(left_depth, right_depth) + 1


# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Maximum Depth:", maxDepth(root))  # Output: 3
