class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)
        count = 0
        for i in range(len(words)):
            if len(words[i]) >= l and pref in words[i][:l]:
                count += 1
        return count
