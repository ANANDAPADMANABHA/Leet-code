class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if n < 3:
            return 0

        good_count = 0

        for i in range(n - 2):
            # Check substring s[i:i+3]
            substring = s[i:i+3]
            if len(set(substring)) == 3:
                good_count += 1

        return good_count
    