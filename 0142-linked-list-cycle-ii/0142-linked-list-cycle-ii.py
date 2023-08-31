# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:                
                slow2 = head
                while slow2 != slow:
                    slow = slow.next
                    slow2 = slow2.next                
                return slow2
        return None
