class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        x = 0
        for i in n:
            if int(i) > x:
                x = int(i)
                
        return x