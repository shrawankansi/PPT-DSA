import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []

    
    for lst in lists:
        if lst:
            heapq.heappush(min_heap, (lst.val, lst))

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        _, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))

    return dummy.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1, list2, list3]

merged_list = mergeKLists(lists)


current = merged_list
while current:
    print(current.val, end="->")
    current = current.next
