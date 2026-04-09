class Solution(object):
    def checkPerfectNumber(self, num):
        sum = 1
        i = 2
        if num == 1:
            return False
        while (i*i <= num):
            if num%i == 0:
                sum += i
                if (i*i!=num):
                    sum += num/i
            i += 1   
        return sum == num
