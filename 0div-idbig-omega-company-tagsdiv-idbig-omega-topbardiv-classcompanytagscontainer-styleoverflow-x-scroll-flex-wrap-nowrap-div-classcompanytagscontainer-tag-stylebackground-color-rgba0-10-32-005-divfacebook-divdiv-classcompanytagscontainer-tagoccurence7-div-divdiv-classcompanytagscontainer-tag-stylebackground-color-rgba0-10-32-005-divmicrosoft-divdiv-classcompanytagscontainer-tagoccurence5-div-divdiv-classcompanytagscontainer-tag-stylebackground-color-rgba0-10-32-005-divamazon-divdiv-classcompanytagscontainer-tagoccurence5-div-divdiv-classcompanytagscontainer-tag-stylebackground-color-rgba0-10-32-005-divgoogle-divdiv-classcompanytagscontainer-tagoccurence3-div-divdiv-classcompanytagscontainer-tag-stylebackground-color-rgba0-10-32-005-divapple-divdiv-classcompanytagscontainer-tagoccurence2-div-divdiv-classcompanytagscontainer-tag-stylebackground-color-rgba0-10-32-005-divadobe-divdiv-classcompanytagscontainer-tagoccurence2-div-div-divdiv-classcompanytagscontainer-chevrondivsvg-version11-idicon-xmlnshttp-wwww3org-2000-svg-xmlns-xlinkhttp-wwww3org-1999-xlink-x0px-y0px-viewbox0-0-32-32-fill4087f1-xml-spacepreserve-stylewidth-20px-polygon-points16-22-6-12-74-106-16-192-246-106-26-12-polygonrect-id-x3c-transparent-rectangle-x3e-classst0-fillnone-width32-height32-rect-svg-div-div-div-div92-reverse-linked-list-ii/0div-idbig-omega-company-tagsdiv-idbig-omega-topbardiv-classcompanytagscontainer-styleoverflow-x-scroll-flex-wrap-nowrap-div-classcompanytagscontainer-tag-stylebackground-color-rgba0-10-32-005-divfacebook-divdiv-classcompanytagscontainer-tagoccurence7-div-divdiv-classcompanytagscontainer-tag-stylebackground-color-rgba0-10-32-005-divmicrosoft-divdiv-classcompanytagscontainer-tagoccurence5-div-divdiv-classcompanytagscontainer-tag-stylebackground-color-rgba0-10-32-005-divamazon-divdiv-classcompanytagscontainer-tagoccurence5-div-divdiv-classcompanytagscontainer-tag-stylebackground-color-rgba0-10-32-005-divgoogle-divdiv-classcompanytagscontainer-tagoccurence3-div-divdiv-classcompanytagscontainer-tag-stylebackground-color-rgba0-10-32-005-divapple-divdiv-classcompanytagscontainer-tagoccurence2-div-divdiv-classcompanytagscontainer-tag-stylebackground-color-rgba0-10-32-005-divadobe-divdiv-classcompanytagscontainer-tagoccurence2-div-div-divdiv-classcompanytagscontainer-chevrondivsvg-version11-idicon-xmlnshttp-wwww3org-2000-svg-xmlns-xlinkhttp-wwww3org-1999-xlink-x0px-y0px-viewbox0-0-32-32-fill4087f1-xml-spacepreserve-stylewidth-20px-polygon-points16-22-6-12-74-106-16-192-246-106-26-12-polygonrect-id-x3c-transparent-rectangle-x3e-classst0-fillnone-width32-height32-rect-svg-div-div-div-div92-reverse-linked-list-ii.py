# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        lst = []
        curNode = head
        while curNode:
            lst.append(curNode)
            curNode = curNode.next

        l,r = left-1,right-1
        while l<r:
            lst[l],lst[r] = lst[r],lst[l]
            l += 1
            r -= 1
        
        for i in range(0,len(lst)-1,1):
            lst[i].next = lst[i+1]
        
        lst[len(lst)-1].next = None
        return lst[0]