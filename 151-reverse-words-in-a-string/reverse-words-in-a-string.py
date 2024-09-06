class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reversed_word = word[::-1]
        ans = ' '.join(reversed_word)
        return ans