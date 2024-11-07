class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        def backtrack(i, str):
            if i == len(digits):
                res.append(str[:])
                return
            
            for letter in letters[digits[i]]:
                backtrack(i + 1, str + letter)
            
        backtrack(0, "")
        
        return res