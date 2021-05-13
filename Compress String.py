class Solution:
    def solve(self, s):
        stack = s[0]
        for c in s:
            if c != stack[-1]:
                stack+=c
        return stack
