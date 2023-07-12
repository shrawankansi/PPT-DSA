class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def connectNodes(root):
    if root is None:
        return root

    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)

            if i < level_size - 1:
                node.next = queue[0]
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

    return root

def printConnections(root):
    current = root

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("-1")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

connected_root = connectNodes(root)


printConnections(connected_root)
