class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[index] = nums[i]
                index +=1
            
        while index < n:
            nums[index] = 0
            index += 1
                
  
        return nums
        