class Solution(object):
    def isThree(self, n):
        for i in range (2,n):
            if n%i==0:
                if i*i==n:
                    return True
                else:
                    return False
        return False
