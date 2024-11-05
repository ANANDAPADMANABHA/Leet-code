class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid] and move both pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If it's 1, just move the mid pointer
                mid += 1
            else:
                # Swap nums[mid] and nums[high] and move high pointer
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
