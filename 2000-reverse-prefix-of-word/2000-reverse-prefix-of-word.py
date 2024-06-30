class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        left, right = 0, len(word) - 1
        found_index = -1

        # Find the index of the first occurrence of ch from the left side
        while left <= right:
            if word[left] == ch:
                found_index = left
                break
            left += 1

        if found_index == -1:
            return word  # Return the original string if `ch` is not found

        # Reverse the segment from start to found_index using two pointers
        left, right = 0, found_index
        word_list = list(word)  # Convert string to list for in-place modifications

        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1

        # Convert list back to string
        result = ''.join(word_list)

        return result