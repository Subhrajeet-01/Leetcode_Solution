class Solution(object):
    def firstUniqChar(self, s):
        
		for i in range(len(s)):
			if s[i] not in s[:i] and s[i] not in s[i+1:]:
				return i
		return -1