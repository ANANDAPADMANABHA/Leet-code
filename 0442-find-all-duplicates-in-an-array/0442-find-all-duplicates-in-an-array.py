class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        while i< n:
            original_index = nums[i]-1
            if nums[original_index] != nums[i]:
                nums[original_index] ,nums[i] = nums[i],nums[original_index]
            else:
                i+=1
        ans = []
        for i in range(n):
            if nums[i]!= i+1:
                ans.append(nums[i])
        return ans