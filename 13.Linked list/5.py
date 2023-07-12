class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteLastOccurrence(head, key):
    if head is None:
        return None

    prev = None
    to_delete = None
    current = head

    while current is not None:
        if current.data == key:
            to_delete = current
        prev = current
        current = current.next

    if to_delete is None:
        return head

    if prev is None:
        head = to_delete.next
    else:
        prev.next = to_delete.next

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(10)

key = 2

new_head = deleteLastOccurrence(head, key)


current = new_head
while current is not None:
    print(current.data, end="->")
    current = current.next
