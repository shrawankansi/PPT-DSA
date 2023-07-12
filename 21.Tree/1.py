class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrderTraversal(root, values):
    if root is None:
        return

    inOrderTraversal(root.left, values)
    values.append(root.val)
    inOrderTraversal(root.right, values)

def convertToBST(values):
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])

    root.left = convertToBST(values[:mid])
    root.right = convertToBST(values[mid+1:])

    return root

def inOrderTraversalBST(root, values):
    if root is None:
        return

    inOrderTraversalBST(root.left, values)
    values.append(root.val)
    inOrderTraversalBST(root.right, values)

def convertBinaryTreeToBST(root):
    values = []
    inOrderTraversal(root, values)
    values.sort()

    bst_root = convertToBST(values)

    return bst_root
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

bst_root = convertBinaryTreeToBST(root)


inorder = []
inOrderTraversalBST(bst_root, inorder)


print(inorder)
