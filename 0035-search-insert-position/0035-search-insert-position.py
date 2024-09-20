class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while high>=low:
            mid = (high+low) //2
            if target == nums[mid]:
                return mid
                
                
            elif target > nums[mid]:
                low = mid+1
                
            else:
                high = mid - 1
                
            
        return low