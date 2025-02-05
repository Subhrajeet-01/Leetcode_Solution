class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 == s2
        count = 0
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                arr.append(i)
            if count > 2:
                return False

        if count == 0:
            return True
        if count == 2 and s1[arr[0]] == s2[arr[1]] and s1[arr[1]] == s2[arr[0]]:
            return True
        
        return False

        