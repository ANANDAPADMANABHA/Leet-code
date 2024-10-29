class Solution(object):
    def canArrange(self, arr, k):
        remainder_count = [0] * k  # Initialize remainder array

        # Step 1: Calculate remainders and update frequencies
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1

        # Step 2: Check the special case for remainder 0
        if remainder_count[0] % 2 != 0:
            return False

        # Step 3: Check pairs of remainders
        for i in range(1, (k // 2) + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False

        return True
