from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])   # start with root in queue
    
    while queue:
        level = []
        for i in range(len(queue)):   # process all nodes at current level
            node = queue.popleft()
            level.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


# Example Tree
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(levelOrder(root))  # [[3], [9, 20], [15, 7]]
