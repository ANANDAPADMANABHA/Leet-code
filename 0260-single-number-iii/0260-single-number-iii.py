class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        x, y = 0, 0
        xor = 0
        n = len(nums)

        # Step 1: XOR of all elements
        for i in range(n):
            xor = xor ^ nums[i]

        # Step 2: Find the rightmost set bit in xor
        lastsetbit = xor & ~(xor - 1)

        # Step 3: Divide the elements into two sets
        for i in range(n):
            if nums[i] & lastsetbit == 0:
                x = x ^ nums[i]
            else:
                y = y ^ nums[i]

        # Return the two unique numbers
        return [x, y]