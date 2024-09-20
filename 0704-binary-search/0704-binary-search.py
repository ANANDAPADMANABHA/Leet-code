class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low  = 0
        while high >= low:
            mid = high+low//2
            
            if nums[mid] == target:
                return  mid
            
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1