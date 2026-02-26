class Solution(object):
    def maxDepth(self, s):
        x=0
        y=0
        for i in s:
            if (i=="("):
                x+=1
            elif (i==")"):
                x-=1
            if y<x:
                y=x
        return y
        
