# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        ans = head
        while head:
            count += 1
            head = head.next
        mid = count // 2
        while mid:
            ans = ans.next
            mid -= 1
        return ans
