class Solution:
    def solve(self, nums):
        if nums.count(1) == 1:
            return True
        c = 1
        mc = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] == 1:
                c+=1
                if c > mc:
                    mc = c
            else:
                c = 1
        return mc == nums.count(1)
