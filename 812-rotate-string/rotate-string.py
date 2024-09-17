class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        from collections import deque
        d = deque(list(s))
        for i in range(len(s)):
            if list(d) == list(goal):
                return True
            d.rotate()
        return False