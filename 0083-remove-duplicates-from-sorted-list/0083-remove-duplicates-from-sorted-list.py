# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
    
        if not head:
            return None
        
        ll = head
        
        while ll.next:
            if ll.val == ll.next.val:
                ll.next = ll.next.next
            else:
                ll = ll.next
        return head