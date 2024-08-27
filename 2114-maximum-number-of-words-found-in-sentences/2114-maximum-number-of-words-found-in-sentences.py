class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_ = 0
        for i in sentences:
            i = i.split(' ')
            if len(i) > max_ :
                max_ = len(i)
        return max_