class Solution:
    def solve(self, nums):
        n = len(nums)
        arr = [x*x for x in nums]
        ans =[]

        l = 0
        r = n-1

        while l <= r:
            if arr[l] > arr[r]:
                ans.append(arr[l])
                l+=1
            else:
                ans.append(arr[r])
                r-=1
        
        return ans[::-1]
