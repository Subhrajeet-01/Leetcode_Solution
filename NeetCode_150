class Solution(object):
    def isValid(self, s):
        S = []
        for i in range(len(s)):
            if s[i] in ['(','[','{']:
                S.append(s[i])
            else:
                if len(S)==0:
                    return False
                if s[i] == ')' and S[-1]!='(':
                    return False
                elif s[i] == ']' and S[-1]!='[':
                
                    return False
                elif s[i] == '}' and S[-1]!='{':
                    return False
                S.pop()
        if len(S)!=0:
            return False       
        return True
