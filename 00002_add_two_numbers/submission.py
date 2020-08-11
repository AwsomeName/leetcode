# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        last = None
        while l1 is not None and l2 is not None:
            val_1 = l1.val
            val_2 = l2.val
            now = ListNode(0)
            now.val = val_1 + val_2
            if last is None:
                head = now
            else:
                last.next = now
            last = now
            l1 = l1.next
            l2 = l2.next
        if l1 is not None:
            if last is not None:
                last.next = l1
            else:
                head = l1
        if l2 is not None:
            if last is not None:
                last.next = l2
            else:
                head = l2
                
    return head
            
      