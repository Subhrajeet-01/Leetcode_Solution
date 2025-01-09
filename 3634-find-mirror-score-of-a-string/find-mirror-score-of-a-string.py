class Solution:
    def calculateScore(self, s: str) -> int:
        def mirror(c):
            i = ord(c) - ord('a')
            return chr(122 - i)
        
        last = collections.defaultdict(list)
        ans = 0
        for i, c in enumerate(s):
            m = mirror(c)
            if last[m]:
                j = last[m].pop()
                ans += i - j
            else:
                last[c].append(i)
        return ans

