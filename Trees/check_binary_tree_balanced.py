class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBalanced(root):
    def check(node):
        if not node:
            return 0   # height = 0 for empty tree

        left = check(node.left)
        if left == -1:   # left subtree not balanced
            return -1
        
        right = check(node.right)
        if right == -1:  # right subtree not balanced
            return -1

        if abs(left - right) > 1:  # height difference > 1 → not balanced
            return -1
        
        return max(left, right) + 1  # return height

    return check(root) != -1


# Example 1 (Balanced)
root1 = Node(3)
root1.left = Node(9)
root1.right = Node(20)
root1.right.left = Node(15)
root1.right.right = Node(7)

print(isBalanced(root1))  # True ✅


# Example 2 (Not Balanced)
root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(3)

print(isBalanced(root2))  # False ❌
