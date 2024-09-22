class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) -1
        
        while high>low:
            mid = (high+low)//2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid +1
                
        return low