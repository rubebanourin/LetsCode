class Solution(object):
    def twoSum(self, nums, target):
        l=len(nums)
        for i in range(l):
            t=target-nums[i]
            for j in range(i+1,l):
                if nums[j]==t:
                    return [i,j]
