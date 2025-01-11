class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        
        hashmap = Counter(s)
        odd_count = 0
        for val in hashmap.values():
            if val % 2 == 1:
                odd_count += 1
        
        return odd_count <= k