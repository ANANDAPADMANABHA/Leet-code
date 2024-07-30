class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if s1 ==s2:
            return True
        count_s1 = {}
        
        
        for i in s1:
            count_s1[i] = count_s1.get(i,0)+1
        
        for i in range(len(s2)-1):
            count_window = {}
            window = s2[i:i+len(s1)]
            for i in window:
                count_window[i]=count_window.get(i,0)+1
            if count_s1 == count_window:
                return True
            
        return False
            
                
                    