class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def leftShift(head, k):
    if head is None or k <= 0:
        return head

    
    current = head
    for _ in range(k - 1):
        if current is None:
            return head
        current = current.next

    if current is None:
        return head

    
    new_head = current

    
    while current.next is not None:
        current = current.next

    
    current.next = head

    
    head = new_head.next
    new_head.next = None

    return head


head = Node(2)
head.next = Node(4)
head.next.next = Node(7)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)

k = 3

new_head = leftShift(head, k)


current = new_head
while current is not None:
    print(current.data, end="->")
    current = current.next
