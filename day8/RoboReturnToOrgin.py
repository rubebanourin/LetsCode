class Solution(object):
    def judgeCircle(self, moves):
        if moves.count('D')==moves.count('U') and moves.count('R')==moves.count('L'):
            return True
        else:
            return False
