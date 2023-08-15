class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        check = 0
        temp = x
        while temp !=0:
            digit = temp % 10
            check = check * 10 + digit
            temp //= 10
        
        return check == x

        