class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        
        while low < high:
            mid = (low+high)//2
            if nums[mid] < nums[high]:
                high = mid  # Move to the left half
            elif nums[mid] > nums[high]:
                low = mid + 1  # Move to the right half
            else:
                # When nums[mid] == nums[high], we can't determine the side, so we reduce high by 1
                high -= 1
                
                
        return nums[low]