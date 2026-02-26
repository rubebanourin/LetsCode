class Solution(object):
    def averageValue(self, nums):
        sum = 0
        count = 0
        for i in nums:
            if i%6 == 0:
                sum += i
                count += 1
        if count == 0:
            return 0
        else:
            return sum/count
