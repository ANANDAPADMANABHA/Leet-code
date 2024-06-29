class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha_num = []
        for i in s:
            if i.isalnum():
                alpha_num.append(i)
        ans = ''.join(alpha_num)
        return ans.lower() == ans[::-1].lower()
