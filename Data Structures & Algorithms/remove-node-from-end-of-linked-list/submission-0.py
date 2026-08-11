# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = ListNode(val = -1, next=head), head
        while n > 0:
            n -= 1
            right = right.next
        
        while right:
            right = right.next
            left = left.next
            
        if left.val == -1:
            return head.next
        left.next = left.next.next
        return head