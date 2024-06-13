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
        counter2 = {}
        for i in s:
            counter[i] = counter.get(i,0)+1
        
        for i in t:
            counter2[i] = counter2.get(i,0)+1
        if counter == counter2:
            return True
        return False