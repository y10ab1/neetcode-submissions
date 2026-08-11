# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse them
        num = 0
        digit = 1
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num += (val1 + val2) * digit
            digit *= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        dummy = head = ListNode()
        for n in str(num)[::-1]:
            head.next = ListNode(int(n))
            head = head.next
        return dummy.next