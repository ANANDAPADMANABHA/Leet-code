class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to store the count of occurrences of each number
        count_dict = {}
        
        # Iterate through the array and count occurrences
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        # Initialize the total count of good pairs
        good_pairs = 0
        
        # Calculate the total count of good pairs
        for count in count_dict.values():
            good_pairs += count * (count - 1) // 2
        
        return good_pairs