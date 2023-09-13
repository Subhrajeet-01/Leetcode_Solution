# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        start = list1
        for _ in range(a-1):
            start = start.next
        end = start
        for _ in range(b-a+1):
            end = end.next
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end.next
        return list1
        