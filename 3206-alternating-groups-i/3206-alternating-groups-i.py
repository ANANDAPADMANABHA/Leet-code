class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        colors += colors[:2]
        output = 0
        len_col = len(colors)
        for i in range(len_col-2):
            block = colors[i:i+3]
            if block == [1,0,1] or block == [0,1,0]:
                output+=1
                
        return output