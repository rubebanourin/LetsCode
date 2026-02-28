class Solution(object):
    def findGCD(self, nums):
        smallest = nums[0]
        largest = nums[0]
        for i in nums:
            if i<smallest:
                smallest = i
            if i>largest:
                largest = i
        while smallest>0:
            remainder=largest%smallest
            if remainder<=0:
                return smallest
            else:
                largest = smallest
                smallest = remainder
