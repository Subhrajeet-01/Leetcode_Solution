# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
    
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False


        # Tortoise and Hare Algorithm
        """
        The idea is that we create two pointers, a slow one and a fast one. The slow pointer traverses the linked list 1 node at a time, while the fast pointer traverses the linked list 2 nodes at a time. If at some point the two pointers meet on the same node, then that means a cycle exists.
        """