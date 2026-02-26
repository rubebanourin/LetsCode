class Solution(object):
    def smallestEvenMultiple(self, n):
        c=n
        while(True):
            if (n%2 == 0):
             return n
            else:
             n+=c
