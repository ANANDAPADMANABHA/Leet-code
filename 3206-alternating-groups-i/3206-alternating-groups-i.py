class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        colors+=colors[:2]
        output = 0
        len_col = len(colors)
        for i in range(len_col-2):
            block = colors[i:i+3]
            if block[0] == block[2] and block[1] != block[0]:
                output += 1
                
        return output