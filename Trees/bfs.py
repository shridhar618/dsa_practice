from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BFS(root):
    if not root:
        return
    
    # create a queue and put the root node
    queue = deque([root])

    while queue:
        node = queue.popleft()  # remove from front
        print(node.val)         # process (print) the node
        
        # add left child if exists
        if node.left:
            queue.append(node.left)
        
        # add right child if exists
        if node.right:
            queue.append(node.right)

# ------------------------
# Example usage:
if __name__ == "__main__":
    # Build a sample tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("BFS Traversal:")
    BFS(root)
