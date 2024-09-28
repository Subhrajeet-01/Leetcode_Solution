class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        current_score = sum(cardPoints[:k])
        max_score = current_score

        for i in range(1, k + 1):
            current_score += cardPoints[-i] - cardPoints[k - i]
            max_score = max(max_score, current_score)
        
        return max_score