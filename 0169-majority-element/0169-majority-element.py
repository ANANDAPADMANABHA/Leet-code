class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0)+1
            
        for char,occurance in counter.items():
            if occurance > len(nums)/2:
                return char
            