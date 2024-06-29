class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1 = 0
        p2 = 0
        ans = []
        while p1<len(s) and p2<len(t):
            if s[p1] == t[p2]:
                ans.append(t[p2])
                p1+=1
                p2+=1
            else:
                p2+=1
                
        return s == ''.join(ans)