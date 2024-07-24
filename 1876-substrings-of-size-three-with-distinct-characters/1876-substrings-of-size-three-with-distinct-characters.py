class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        p1 = 0 
        p2 = 3
        output = []
        while p2<=len(s):
            a = s[p1:p2]
            set_a = set(a)
    
            list_a = list(a)
            if len(list_a) == len(set_a):
                output.append(a)
            p1+=1
            p2+=1
            
        return len(output)
    