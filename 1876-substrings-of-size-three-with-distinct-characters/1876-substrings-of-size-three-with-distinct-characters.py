class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        good_count = 0
        n = len(s)
        for i in range(n-2):
            substring = s[i:i+3]
            if len(set(substring)) == 3:
                good_count +=1
        
        return good_count
    