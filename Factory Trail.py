class Solution:
    def solve(self, n):
        
        ans = 0
        while n > 1:
            n = n // 5
            ans = ans + n
        return ans
