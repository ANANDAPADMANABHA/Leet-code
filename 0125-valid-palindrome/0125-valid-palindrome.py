class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normalized_s = ''.join([ch.lower() for ch in s if ch.isalnum()])
    
        # Step 2: Use two pointers to check palindrome
        if normalized_s == normalized_s[::-1]:
            return True
        return False
