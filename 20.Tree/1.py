class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findMaxSubtreeSum(root):
    global max_sum
    if root is None:
        return 0

    left_sum = findMaxSubtreeSum(root.left)
    right_sum = findMaxSubtreeSum(root.right)

    current_sum = root.val + left_sum + right_sum

    max_sum = max(max_sum, current_sum)

    return current_sum

def findMaximumSubtreeSum(root):
    global max_sum
    max_sum = float('-inf')

    findMaxSubtreeSum(root)

    return max_sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

max_subtree_sum = findMaximumSubtreeSum(root)


print(max_subtree_sum)
