class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.prev = None
        self.next = None

def inOrderTraversal(root):
    global prev
    if root is None:
        return

    inOrderTraversal(root.left)

    if prev is not None:
        prev.next = root
        root.prev = prev

    prev = root

    inOrderTraversal(root.right)

def convertBinaryTreeToDoublyLinkedList(root):
    global prev
    prev = None

    inOrderTraversal(root)

    head = root
    while head and head.left:
        head = head.left

    return head


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

doubly_linked_list_head = convertBinaryTreeToDoublyLinkedList(root)


current = doubly_linked_list_head
while current:
    print(current.val, end=" ")
    current = current.next

