class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = 0
        for i in range(len(word)):
            if word[i]==ch:
                index = i
                break
                
        return word[index::-1]+word[index+1:]