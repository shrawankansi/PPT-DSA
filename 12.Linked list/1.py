class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if head is None or head.next is None:
        return False

    tortoise = head
    hare = head.next

    while tortoise != hare:
        if hare is None or hare.next is None:
            return False

        tortoise = tortoise.next
        hare = hare.next.next

    return True


head = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
head.next = node2
node2.next = node3
node3.next = head  

print(hasCycle(head))  # Output: True
