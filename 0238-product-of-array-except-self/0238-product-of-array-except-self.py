class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        curr = 1
        for i in range(n):
            ans[i] = ans[i] * curr
            curr = curr * nums[i]

        curr = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * curr
            curr = curr * nums[i]

        return ans
        