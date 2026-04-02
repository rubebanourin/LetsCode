class Solution(object):
    def differenceOfSum(self, nums):
        e = 0
        d = 0
        for num in nums:
            e = e+num
            while num>0:
                d = d+(num%10)
                num/=10
        return abs(e-d)
