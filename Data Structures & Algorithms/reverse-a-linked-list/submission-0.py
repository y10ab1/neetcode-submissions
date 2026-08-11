# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        pre, cur, post = None, head, head.next
        
        while cur is not None:
            cur.next = pre
            pre = cur
            cur = post
            post = post.next if post is not None else post
        return pre