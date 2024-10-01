class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        frequency = 0
        start = 0
        maxlen = 0
        for end, char in enumerate(s):
            hashmap[char] = hashmap.get(char, 0) + 1
            frequency = max(frequency, hashmap[char])
            if (end - start + 1) - frequency > k:
                hashmap[s[start]] -= 1
                start += 1
            maxlen = max(maxlen, end - start + 1)
        return maxlen