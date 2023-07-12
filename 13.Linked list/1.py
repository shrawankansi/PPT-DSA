class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createNewList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    new_head = None
    current = None

    while head1 is not None and head2 is not None:
        
        if head1.data >= head2.data:
            new_node = Node(head1.data)
            head1 = head1.next
        else:
            new_node = Node(head2.data)
            head2 = head2.next

        if new_head is None:
            new_head = new_node
            current = new_head
        else:
            current.next = new_node
            current = current.next

    
    if head1 is not None:
        current.next = head1
    if head2 is not None:
        current.next = head2

    return new_head



head1 = Node(5)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(8)


head2 = Node(1)
head2.next = Node(7)
head2.next.next = Node(4)
head2.next.next.next = Node(5)

new_head = createNewList(head1, head2)


current = new_head
while current is not None:
    print(current.data, end="->")
    current = current.next
