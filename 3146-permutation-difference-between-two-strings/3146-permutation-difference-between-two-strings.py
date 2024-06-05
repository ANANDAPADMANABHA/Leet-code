class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        index_s = {char: idx for idx, char in enumerate(s)}
        index_t = {char: idx for idx, char in enumerate(t)}

        difference = 0
        for char in s:
            difference += abs(index_s[char] - index_t[char])

        return difference