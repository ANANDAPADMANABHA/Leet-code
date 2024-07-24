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
            x = []
            a = s[p1:p2]
            for i in a:
                if i in x:
                    '''repeated balue'''
                    break
                x.append(i)
            else:
                output.append(a)
            p1+=1
            p2+=1
            
        return len(output)