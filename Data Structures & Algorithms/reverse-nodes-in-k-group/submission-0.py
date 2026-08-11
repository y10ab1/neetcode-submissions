# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reveresedList = []
        dummy = ListNode(next = head)
        groupprev = dummy
        while True:
            kth = self.getKth(groupprev,k)
            if not kth:
                break
            groupnext = kth.next

            newend = self.reverse(groupprev.next, groupnext)
            newend.next = groupnext
            groupprev.next = kth
            groupprev = newend
        return dummy.next
        



    def getKth(self,start,k):
        while start and k > 0:
            start = start.next
            k -= 1
        return start

    def reverse(self, head, end):
        pre = None
        cur = head
        nxt = cur.next
        while cur != end:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return head