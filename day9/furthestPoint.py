class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        l=moves.count('L')
        r=moves.count('R')
        b=moves.count('_')
        if l>r:
            return l-r+b
        else:
            return r-l+b
