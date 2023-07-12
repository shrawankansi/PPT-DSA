class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addOne(head):
    if head is None:
        return None

    
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev

    
    carry = 1
    current = head
    while current is not None:
        sum = current.data + carry
        current.data = sum % 10
        carry = sum // 10
        current = current.next

    
    if carry == 1:
        new_node = Node(1)
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node

    
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev

    return head


head = Node(4)
head.next = Node(5)
head.next.next = Node(6)

new_head = addOne(head)


current = new_head
while current is not None:
    print(current.data, end="->")
    current = current.next
