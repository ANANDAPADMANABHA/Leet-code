class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            p1,p2 =0,len(i)-1
            word_list = list(i)
            while p1<p2:
                word_list[p1],word_list[p2] = word_list[p2],word_list[p1]
                p1+=1
                p2-=1
                
            word_string = ''.join(word_list)
            if word_string == i:
                return i
        return ''
            
            