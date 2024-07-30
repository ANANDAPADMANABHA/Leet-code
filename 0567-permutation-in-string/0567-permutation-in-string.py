class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        count_s1 = {}
        count_window = {}

        # Initialize the count for s1 and the first window of s2
        for i in range(len_s1):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1
            count_window[s2[i]] = count_window.get(s2[i], 0) + 1

        # Check the initial window
        if count_s1 == count_window:
            return True

        # Slide the window over s2
        for i in range(len_s1, len_s2):
            start_char = s2[i - len_s1]
            new_char = s2[i]

            # Update the count for the new character in the window
            count_window[new_char] = count_window.get(new_char, 0) + 1
            
            # Update the count for the old character that is no longer in the window
            if count_window[start_char] == 1:
                del count_window[start_char]
            else:
                count_window[start_char] -= 1

            # Check if the current window's character counts match s1's character counts
            if count_s1 == count_window:
                return True

        return False
