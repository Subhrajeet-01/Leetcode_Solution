class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for char in count.keys():
            if count[char] % 2 == 0:
                res += 2
            else:
                res += 1
        
        return res