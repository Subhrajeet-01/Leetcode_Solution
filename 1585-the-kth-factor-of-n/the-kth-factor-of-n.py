class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = [1]
        for i in range(2, (n//2)+1):
            if n % i == 0:
                arr.append(i)
        arr.append(n)
        print(arr)
        if k - 1 <= len(arr) - 1:
            return arr[k - 1]
        return -1
                