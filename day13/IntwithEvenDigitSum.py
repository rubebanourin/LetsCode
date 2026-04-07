class Solution(object):
    def countEven(self, num):
        count = 0
        for i in range(num,0,-1):
            sum = 0
            while i>0:
                sum += i%10
                i /= 10
            if sum%2 == 0:
                count +=1
        return count
