# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        last = None
        ctr = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                val_1 = 0
            else:
                val_1 = l1.val
                l1 = l1.next
                
            if l2 is None:
                val_2 = 0
            else:
                val_2 = l2.val
                l2 = l2.next
                
            tmp = val_1 + val_2 + ctr
            now = ListNode(tmp % 10)
            ctr = tmp // 10
            
            if last is None:
                head = now
            else:
                last.next = now
            last = now
        if ctr == 1:
            now = ListNode(1)
            last.next = now
        return head
      