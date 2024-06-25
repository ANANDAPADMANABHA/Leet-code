class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        vowel_list = []
        vowel_indices = []
        
        # Step 1: Extract vowels and their indices
        for i, char in enumerate(s):
            if char in vowels:
                vowel_list.append(char)
                vowel_indices.append(i)
        
        # Step 2: Sort the vowels
        vowel_list.sort()
        
        # Step 3: Create the result list and place the sorted vowels
        result = list(s)
        for i, index in enumerate(vowel_indices):
            result[index] = vowel_list[i]
        
        return ''.join(result)