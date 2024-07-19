class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_xor = 0
        n = len(nums)

        # Use sliding window approach
        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)
                else:
                    # Since the array is sorted, no need to check further in this inner loop
                    break

        return max_xor