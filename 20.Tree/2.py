class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructBST(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    i = 1

    while i < len(level_order):
        node = queue.pop(0)

        left_val = level_order[i]
        left_child = TreeNode(left_val)
        node.left = left_child
        queue.append(left_child)
        i += 1

        if i < len(level_order):
            right_val = level_order[i]
            right_child = TreeNode(right_val)
            node.right = right_child
            queue.append(right_child)
            i += 1

    return root

def inorderTraversal(root):
    if root is None:
        return []

    result = []
    stack = []

    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)

        current = current.right

    return result



level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]

root = constructBST(level_order)


inorder = inorderTraversal(root)
print(inorder)
