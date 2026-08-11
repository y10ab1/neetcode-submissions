# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at middle
        # reverse the second half

        pre, second = None, slow
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        first, second = head, pre

        while first and second:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp

        


