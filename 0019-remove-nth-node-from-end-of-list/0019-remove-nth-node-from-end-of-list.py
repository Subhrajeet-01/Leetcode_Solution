# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        current = head
        cur = head
        count = 0
        while current:
            count += 1
            current = current.next
        x = count - n - 1
        y = 0
        if x == -1:
            return cur.next
        while cur:
            if x == y:
                cur.next = cur.next.next
                break
            cur = cur.next
            y += 1
        return head
        