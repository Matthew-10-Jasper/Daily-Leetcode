class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(10):
            n-= (10-i)
            if n<0 and ((10-i)%2==0):
                return False
            elif n<0:
                return True
        