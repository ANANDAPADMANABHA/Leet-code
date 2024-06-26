class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0)+1
        
        output = []
        for char,occurance in counter.items():
            if occurance > len(nums)/3:
                output.append(char)
                
        return output