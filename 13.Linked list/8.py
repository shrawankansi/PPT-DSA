class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteNode(head, position):
    if head is None:
        return head

    if position == 1:
        new_head = head.next
        if new_head is not None:
            new_head.prev = None
        return new_head

    current = head
    prev = None

    
    for _ in range(position - 1):
        if current is None:
            return head  
        prev = current
        current = current.next

    if current is None:
        return head  

    
    prev.next = current.next
    if current.next is not None:
        current.next.prev = prev

    return head


head = Node(1)
node2 = Node(3)
node3 = Node(4)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

position = 3

new_head = deleteNode(head, position)


current = new_head
while current is not None:
    print(current.data, end=" <--> ")
    current = current.next
