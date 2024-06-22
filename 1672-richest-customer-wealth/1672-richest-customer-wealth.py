class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        richest = 0
        for i in accounts:
            wealth = 0
            for j in i:
                wealth +=j

            if richest < wealth:
                richest = wealth

        return richest