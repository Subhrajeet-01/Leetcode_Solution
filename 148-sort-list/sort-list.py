# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ans =[]
        while curr:
            ans.append(curr.val)
            curr = curr.next
        ans.sort()
        curr = head
        for i in ans:
            curr.val = i
            curr = curr.next
        return head