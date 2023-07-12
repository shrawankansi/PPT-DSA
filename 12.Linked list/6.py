class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNodes(head, M, N):
    if head is None or M <= 0 or N <= 0:
        return head

    current = head
    previous = None

    while current is not None:
    
        for _ in range(M):
            if current is None:
                return head  
            previous = current
            current = current.next

        
        for _ in range(N):
            if current is None:
                break  
            current = current.next

        
        previous.next = current

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)

M = 3
N = 2

new_head = deleteNodes(head, M, N)


current = new_head
while current is not None:
    print(current.data, end="->")
    current = current.next

