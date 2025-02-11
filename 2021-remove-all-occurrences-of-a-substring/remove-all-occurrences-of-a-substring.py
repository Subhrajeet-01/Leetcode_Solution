class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            start_index = s.find(part)
            s = s[:start_index] + s[start_index + len(part):]

        return s