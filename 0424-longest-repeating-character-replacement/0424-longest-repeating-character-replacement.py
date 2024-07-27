class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        max_freq =0
        count = {}
        max_length = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_freq = max(count[s[right]],max_freq)
            
            if (right -left+1) - max_freq > k:
                count[s[left]]-=1
                left +=1
                
            max_length = max(max_length,right -left+1)
                
        return max_length