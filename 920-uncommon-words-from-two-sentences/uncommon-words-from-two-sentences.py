class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_s1 = s1.split()
        word_s2 = s2.split()
        all_words = word_s1 + word_s2
        word_count = Counter(all_words)
        ans = []
        for ele in word_count.keys():
            if word_count[ele] == 1:
                ans.append(ele)
        return ans