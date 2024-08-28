class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        i = 0
        while i<n:
            correct_index =  nums[i] -1
        
            if nums[i] != nums[correct_index]:
                nums[i] ,nums[correct_index] = nums[correct_index],nums[i]
            else:
                i+=1
                
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]                   
                
            
            