class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        for element in nums:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
                
        max_frequency = max(frequency.values())
        
        count = sum(freq for freq in frequency.values() if freq == max_frequency)
        
        return count