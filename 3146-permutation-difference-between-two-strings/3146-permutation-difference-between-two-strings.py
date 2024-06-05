class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    ans += (i-j if i>j else j-i)
                    break
                    
        return ans