class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        sum=0
        n = x
        while x>0:
            sum += x%10
            x /= 10
        if n%sum == 0:
            return sum
        else:
            return -1
