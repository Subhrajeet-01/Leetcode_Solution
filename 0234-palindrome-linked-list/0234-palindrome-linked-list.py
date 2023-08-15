# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        curr = head
        value = [head.val]
        while curr.next:
            curr = curr.next
            value.append(curr.val)
        return value == value[::-1]