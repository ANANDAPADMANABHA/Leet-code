class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0)+1
        
        for i in t:
            if i not in  counter:
                return False
            counter[i] -= 1
            
            if counter[i]<0:
                return False
        
        return True