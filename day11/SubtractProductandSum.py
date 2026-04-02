class Solution(object):
    def subtractProductAndSum(self, n):
        s = 0
        p = 1
        while n>0:
            p = p*(n%10)
            s = s+(n%10)
            n = n/10
        return p-s
