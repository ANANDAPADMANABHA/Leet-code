class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        if index == -1:
            return word  # Return the original string if `ch` is not found

        # Convert the string to a list to perform in-place modifications
        word_list = list(word)

        # Initialize two pointers
        left, right = 0, index

        # Perform the in-place reversal using two pointers
        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1

        # Convert the list back to a string
        result = ''.join(word_list)

        return result